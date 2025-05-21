# KPI Dashboard for Software Quality Management

## Overview

This application is a comprehensive dashboard for monitoring and evaluating software quality metrics in high-assurance software development environments. It's designed for quality assurance teams to track key performance indicators (KPIs), manage project risks, and provide feedback on the usefulness of various metrics.

## Features

### 1. KPI Monitoring and Visualization
- Interactive charting of various software quality metrics over time
- Visual status indicators showing performance against targets
- Support for multiple KPI types including:
  - Defect density
  - Test coverage
  - Mean time to detect (MTTD)
  - Defect injection rate
  - Detection rate
  - Review efficiency
  - Checklist adherence

### 2. Risk Management
- Interactive risk matrix visualization
- Risk categorization based on likelihood and impact
- Color-coded risk severity indicators (green, yellow, orange, red)
- Ability to add predefined risks to the current project context
- Custom assignment of likelihood and impact values

### 3. Metric Evaluation System
- Framework for evaluating the usefulness of different metrics
- Structured approach to identify valuable vs. non-valuable metrics
- Justification capture for evaluation decisions
- Submission of feedback to inform future metric selection

## Technical Architecture

### Frontend
- Built with React (using Hooks for state management)
- Chart.js for data visualization
- CSS for styling

### Backend Integration
- RESTful API integration for data fetching and submission
- Endpoints:
  - `/api/kpi` - Retrieves KPI data
  - `/api/kpi_targets` - Retrieves target values for KPIs
  - `/api/risks` - Gets and posts risk data
  - `/api/predefined_risks` - Retrieves predefined risk templates
  - `/api/feedback-submission` - Submits metric evaluation feedback

## Component Structure

The application consists of a single `App` component that handles all functionality, including:

1. **State Management**:
   - KPI data and targets
   - Risk data and predefined risks
   - User selections and inputs
   - Form submission status

2. **Data Visualization**:
   - Line charts for KPI trend visualization
   - Color-coded risk matrix

3. **User Interface Sections**:
   - KPI selector and chart display
   - Metric definitions and descriptions
   - Metric evaluation interface
   - Risk matrix visualization
   - Risk submission form

## Getting Started

### Prerequisites
- Node.js and npm installed
- Backend API server running (see Backend Setup)

### Installation

1. Clone the repository:
   ```
   git clone https://your-repository-url.git
   cd kpi-dashboard
   ```

2. Install dependencies:
   ```
   npm install
   ```

3. Start the development server:
   ```
   npm start
   ```

4. Open your browser to `http://localhost:3000`

### Backend Setup

The application requires a backend server that provides the following API endpoints:

- GET `/api/kpi` - Returns JSON object with KPI data series
- GET `/api/kpi_targets` - Returns JSON object with target values for each KPI
- GET `/api/risks` - Returns array of current risks
- GET `/api/predefined_risks` - Returns array of predefined risk templates
- POST `/api/risks` - Adds a new risk
- POST `/api/feedback-submission` - Submits feedback on metric evaluation

The backend should store data in JSON files as indicated by the API integration in the frontend code.

## Usage Guide

### KPI Monitoring

1. Select a KPI from the dropdown menu to view its trend over time
2. The chart will display the selected KPI's data over recent sprints
3. Below the chart, you can see:
   - Latest value
   - Target value
   - Status (GREEN if meeting target, RED if not)

### Metric Evaluation

1. Review the definitions of each metric in the "Metric Definitions and Importance" section
2. Consider the guiding questions:
   - Does this metric influence actual quality or just track activity?
   - Can this metric be gamed easily?
   - Does this help identify risks early or improve team behavior?
3. Select up to 3 metrics you consider valuable
4. Select up to 3 metrics you consider not valuable
5. Provide justification for your selections in the text area
6. Submit your evaluation

### Risk Management

1. View current project risks in the risk matrix
   - Risks are positioned based on likelihood (1-5) and impact (1-5)
   - Cell colors indicate risk severity (green, yellow, orange, red)
2. To add a new risk:
   - Select from the predefined risks dropdown
   - Assign likelihood (1-5)
   - Assign impact (1-5)
   - Click "Add Risk"
3. The risk matrix will update automatically after submission

## Contributing

Guidelines for contributing to this project:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

## License

[Specify license information here]