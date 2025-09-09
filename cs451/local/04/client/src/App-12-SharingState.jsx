<pre class="code_syntax" style="color:#000000;background:#ffffff;"><span class="line_wrapper"><span style="color:#696969; ">// Section10-SharingState.js</span></span>
<span class="line_wrapper"><span style="color:#696969; ">// </span><span style="color:#5555dd; ">https://react.dev/learn/managing-state#sharing-state-between-components</span></span>
<span class="line_wrapper"><span style="color:#800000; font-weight:bold; ">import</span> <span style="color:#800080; ">{</span> useState <span style="color:#800080; ">}</span> from <span style="color:#800000; ">'</span><span style="color:#0000e6; ">react</span><span style="color:#800000; ">'</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper"><span style="color:#800000; font-weight:bold; ">export</span> <span style="color:#800000; font-weight:bold; ">default</span> <span style="color:#800000; font-weight:bold; ">function</span> Accordion<span style="color:#808030; ">(</span><span style="color:#808030; ">)</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">const</span> <span style="color:#808030; ">[</span>activeIndex<span style="color:#808030; ">,</span> setActiveIndex<span style="color:#808030; ">]</span> <span style="color:#808030; ">=</span> useState<span style="color:#808030; ">(</span><span style="color:#008c00; ">0</span><span style="color:#808030; ">)</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">return</span> <span style="color:#808030; ">(</span></span>
<span class="line_wrapper">    <span style="color:#808030; ">&lt;</span><span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>h2<span style="color:#808030; ">&gt;</span>Almaty<span style="color:#808030; ">,</span> Kazakhstan<span style="color:#808030; ">&lt;</span><span style="color:#808030; ">/</span>h2<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>Panel</span>
<span class="line_wrapper">        title<span style="color:#808030; ">=</span><span style="color:#800000; ">"</span><span style="color:#0000e6; ">About</span><span style="color:#800000; ">"</span></span>
<span class="line_wrapper">        isActive<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>activeIndex <span style="color:#808030; ">===</span> <span style="color:#008c00; ">0</span><span style="color:#800080; ">}</span></span>
<span class="line_wrapper">        onShow<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span><span style="color:#808030; ">(</span><span style="color:#808030; ">)</span> <span style="color:#808030; ">=</span><span style="color:#808030; ">&gt;</span> setActiveIndex<span style="color:#808030; ">(</span><span style="color:#008c00; ">0</span><span style="color:#808030; ">)</span><span style="color:#800080; ">}</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#797997; ">With</span> a population of about <span style="color:#008c00; ">2</span> million<span style="color:#808030; ">,</span> Almaty is Kazakhstan<span style="color:#800000; ">'</span><span style="color:#0000e6; ">s largest city. From 1929 to 1997, it was its capital city.</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;/Panel&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;Panel</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        title="Etymology"</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        isActive={activeIndex === 1}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        onShow={() =&gt; setActiveIndex(1)}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        The name comes from &lt;span lang="kk-KZ"&gt;алма&lt;/span&gt;, the Kazakh word for "apple" and is often translated as "full of apples". In fact, the region surrounding Almaty is thought to be the ancestral home of the apple, and the wild &lt;i lang="la"&gt;Malus sieversii&lt;/i&gt; is considered a likely candidate for the ancestor of the modern domestic apple.</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;/Panel&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">    &lt;/&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">  );</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; "></span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">function Panel({ title, children, isActive, onShow }) {</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">  return (</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">    &lt;section className="panel"&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;h3&gt;{title}&lt;/h3&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      {isActive ? (</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        &lt;p&gt;{children}&lt;/p&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      ) : (</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        &lt;button onClick={onShow}&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">          Show</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        &lt;/button&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      )}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">    &lt;/section&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">  );</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">}</span></span></pre>