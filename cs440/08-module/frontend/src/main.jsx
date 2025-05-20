// main.jsx (Improved risk submission with matrix position selection)

import React, { useEffect, useState, useRef } from 'react';
import { createRoot } from 'react-dom/client';
import Chart from 'chart.js/auto';
import './style.css';

function App() {
  const [kpiData, setKpiData] = useState({});
  const [kpiTargets, setKpiTargets] = useState({});
  const [selectedKPI, setSelectedKPI] = useState('defect_density');
  const [riskData, setRiskData] = useState([]);
  const [selectedValuable, setSelectedValuable] = useState([]);
  const [selectedNotValuable, setSelectedNotValuable] = useState([]);
  const [justification, setJustification] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [selectedRisk, setSelectedRisk] = useState('');
  const [customLikelihood, setCustomLikelihood] = useState('');
  const [customImpact, setCustomImpact] = useState('');

  const chartRef = useRef(null);
  const chartInstance = useRef(null);

  const predefinedRisks = [
    { id: 'R004', description: 'Inconsistent unit testing' },
    { id: 'R005', description: 'Developer turnover' },
    { id: 'R006', description: 'Delayed code reviews' },
    { id: 'R007', description: 'Dependency on unstable third-party libraries' },
    { id: 'R008', description: 'Poor documentation in legacy modules' }
  ];

  const metricDescriptions = {
    defect_density: "Defects per 1000 lines of code.",
    test_coverage: "Percentage of code tested by automated tests.",
    mttd: "Mean Time to Detect: Average time to find a defect.",
    injection_rate: "How frequently defects are introduced during development.",
    detection_rate: "How effectively developers detect their own defects.",
    review_efficiency: "How effective peer reviews are at catching issues.",
    checklist_adherence: "Extent to which developers follow process checklists."
  };

  useEffect(() => {
    fetch('/api/kpi').then(res => res.json()).then(setKpiData);
    fetch('/api/kpi_targets').then(res => res.json()).then(setKpiTargets);
    fetch('/api/risks').then(res => res.json()).then(setRiskData);
  }, []);

  useEffect(() => {
    if (kpiData[selectedKPI] && kpiTargets[selectedKPI] != null && chartRef.current) {
      if (chartInstance.current) chartInstance.current.destroy();
      chartInstance.current = new Chart(chartRef.current.getContext('2d'), {
        type: 'line',
        data: {
          labels: ['Sprint 1', 'Sprint 2', 'Sprint 3', 'Sprint 4'],
          datasets: [{
            label: selectedKPI,
            data: kpiData[selectedKPI],
            borderColor: 'blue',
            backgroundColor: 'lightblue',
            tension: 0.3
          }]
        }
      });
    }
  }, [kpiData, kpiTargets, selectedKPI]);

  function getStatus(value, target, isHigherBetter) {
    if (isHigherBetter) return value >= target ? 'green' : 'red';
    return value <= target ? 'green' : 'red';
  }

  function getColor(l, i) {
    const score = l * i;
    if (score <= 4) return 'green';
    if (score <= 9) return 'yellow';
    if (score <= 16) return 'orange';
    return 'red';
  }

  function renderMatrix() {
    const matrix = Array.from({ length: 5 }, () => Array.from({ length: 5 }, () => []));
    riskData.forEach(r => {
      matrix[r.likelihood - 1][r.impact - 1].push(r);
    });
    return matrix.flatMap((row, i) =>
      row.map((cell, j) => (
        <div key={`${i}-${j}`} className={`matrix-cell ${getColor(i + 1, j + 1)}`}>
          {cell.map(r => (
            <div key={r.id}><strong>{r.id}</strong>: {r.description}</div>
          ))}
        </div>
      ))
    );
  }

  function toggleMetric(metric, setList) {
    setList(prev => prev.includes(metric)
      ? prev.filter(m => m !== metric)
      : [...prev, metric]
    );
  }

  function handleSubmit() {
    const data = {
      valuable: selectedValuable,
      not_valuable: selectedNotValuable,
      justification,
      timestamp: new Date().toISOString()
    };
    fetch('/api/metric-submission', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    }).then(() => setSubmitted(true));
  }

  function submitRisk() {
    const selected = predefinedRisks.find(r => r.id === selectedRisk);
    if (!selected || !customLikelihood || !customImpact) return;
    const newRisk = {
      ...selected,
      likelihood: parseInt(customLikelihood),
      impact: parseInt(customImpact)
    };
    fetch('/api/risks', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(newRisk)
    }).then(() => {
      setRiskData(prev => [...prev, newRisk]);
      setSelectedRisk('');
      setCustomLikelihood('');
      setCustomImpact('');
    });
  }

  if (!kpiData[selectedKPI]) return <p>Loading...</p>;
  const current = kpiData[selectedKPI].at(-1);
  const target = kpiTargets[selectedKPI];
  const isHigher = selectedKPI === 'test_coverage';
  const status = getStatus(current, target, isHigher);

  return (
    <div className="container">
      <h1>KPI Dashboard</h1>
      <p><strong>Scenario:</strong> You have joined a quality assurance team at a high-assurance software organization like Rolls-Royce. The company monitors a wide range of software quality metrics including defect density, test coverage, and developer checklist adherence. Your task is to evaluate these metrics and identify which ones provide actionable insights for improving software quality.</p>

      <select onChange={e => setSelectedKPI(e.target.value)} value={selectedKPI}>
        {Object.keys(kpiData).map(metric => (
          <option key={metric} value={metric}>{metric}</option>
        ))}
      </select>

      <canvas ref={chartRef} width="600" height="300"></canvas>
      <div>
        <strong>Latest:</strong> {current} | <strong>Target:</strong> {target} | 
        <span style={{ color: status, fontWeight: 'bold' }}>{status.toUpperCase()}</span>
      </div>

      <h2 className="mt-6">Metric Definitions and Importance</h2>
      <ul>
        {Object.entries(metricDescriptions).map(([metric, desc]) => (
          <li key={`def-${metric}`}><strong>{metric}</strong>: {desc}</li>
        ))}
      </ul>

      <h2 className="mt-6">Select Metrics for Evaluation</h2>
      <p><em>Use these questions to guide your selection:</em></p>
      <ul>
        <li>Does this metric influence actual quality or just track activity?</li>
        <li>Can this metric be gamed easily?</li>
        <li>Does this help identify risks early or improve team behavior?</li>
      </ul>

      <div style={{ display: 'flex', gap: '2rem', marginTop: '1rem' }}>
        <div>
          <h3>Valuable Metrics (Pick 3)</h3>
          {Object.keys(metricDescriptions).map((metric) => (
            <div key={`v-${metric}`}>
              <label>
                <input
                  type="checkbox"
                  checked={selectedValuable.includes(metric)}
                  onChange={() => toggleMetric(metric, setSelectedValuable)}
                /> {metric}
              </label>
            </div>
          ))}
        </div>
        <div>
          <h3>Not Valuable Metrics (Pick 3)</h3>
          {Object.keys(metricDescriptions).map((metric) => (
            <div key={`nv-${metric}`}>
              <label>
                <input
                  type="checkbox"
                  checked={selectedNotValuable.includes(metric)}
                  onChange={() => toggleMetric(metric, setSelectedNotValuable)}
                /> {metric}
              </label>
            </div>
          ))}
        </div>
      </div>

      <div style={{ marginTop: '1rem' }}>
        <label>
          <h3>Justify your selections:</h3>
          <textarea
            rows="5"
            cols="80"
            placeholder="Explain why you chose these metrics as valuable or not valuable."
            value={justification}
            onChange={(e) => setJustification(e.target.value)}
          ></textarea>
        </label>
      </div>

      <button style={{ marginTop: '1rem' }} onClick={handleSubmit} disabled={submitted}>
        {submitted ? 'Submitted' : 'Submit Evaluation'}
      </button>

      <h2 style={{ marginTop: '3rem' }}>Risk Matrix</h2>
      <p><strong>Scenario:</strong> Your software project has just entered a critical delivery phase. As a QA leader, you must proactively assess and visualize technical risks that could affect performance, stability, or team coordination. Below is the matrix showing the severity of risks based on their likelihood and impact. You may submit additional risks from a common library to improve situational awareness.</p>

      <div style={{ marginTop: '2rem', marginBottom: '1rem' }}>
        <h3>Submit a Risk to the Matrix</h3>
        <select value={selectedRisk} onChange={e => setSelectedRisk(e.target.value)}>
          <option value="">Select a risk to add...</option>
          {predefinedRisks.map(risk => (
            <option key={risk.id} value={risk.id}>{risk.id} - {risk.description}</option>
          ))}
        </select>
        <span style={{ marginLeft: '1rem' }}>Likelihood:</span>
        <select value={customLikelihood} onChange={e => setCustomLikelihood(e.target.value)}>
          <option value="">--</option>
          {[1, 2, 3, 4, 5].map(n => <option key={n} value={n}>{n}</option>)}
        </select>
        <span style={{ marginLeft: '1rem' }}>Impact:</span>
        <select value={customImpact} onChange={e => setCustomImpact(e.target.value)}>
          <option value="">--</option>
          {[1, 2, 3, 4, 5].map(n => <option key={n} value={n}>{n}</option>)}
        </select>
        <button style={{ marginLeft: '1rem' }} onClick={submitRisk} disabled={!selectedRisk || !customLikelihood || !customImpact}>
          Add Risk
        </button>
      </div>

      <div className="matrix-grid">
        {renderMatrix()}
      </div>
    </div>
  );
}

const root = createRoot(document.getElementById('root'));
root.render(<App />);
