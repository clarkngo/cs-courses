<pre class="code_syntax" style="color:#000000;background:#ffffff;"><span class="line_wrapper"><span style="color:#696969; ">// Section06-UpdatingObjects.js</span></span>
<span class="line_wrapper"><span style="color:#696969; ">// </span><span style="color:#5555dd; ">https://react.dev/learn/adding-interactivity#updating-objects-in-state</span></span>
<span class="line_wrapper"><span style="color:#800000; font-weight:bold; ">import</span> <span style="color:#800080; ">{</span> useState <span style="color:#800080; ">}</span> from <span style="color:#800000; ">'</span><span style="color:#0000e6; ">react</span><span style="color:#800000; ">'</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper"><span style="color:#800000; font-weight:bold; ">export</span> <span style="color:#800000; font-weight:bold; ">default</span> <span style="color:#800000; font-weight:bold; ">function</span> Form<span style="color:#808030; ">(</span><span style="color:#808030; ">)</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">const</span> <span style="color:#808030; ">[</span>person<span style="color:#808030; ">,</span> setPerson<span style="color:#808030; ">]</span> <span style="color:#808030; ">=</span> useState<span style="color:#808030; ">(</span><span style="color:#800080; ">{</span></span>
<span class="line_wrapper">    name<span style="color:#800080; ">:</span> <span style="color:#800000; ">'</span><span style="color:#0000e6; ">Niki de Saint Phalle</span><span style="color:#800000; ">'</span><span style="color:#808030; ">,</span></span>
<span class="line_wrapper">    artwork<span style="color:#800080; ">:</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">      title<span style="color:#800080; ">:</span> <span style="color:#800000; ">'</span><span style="color:#0000e6; ">Blue Nana</span><span style="color:#800000; ">'</span><span style="color:#808030; ">,</span></span>
<span class="line_wrapper">      city<span style="color:#800080; ">:</span> <span style="color:#800000; ">'</span><span style="color:#0000e6; ">Hamburg</span><span style="color:#800000; ">'</span><span style="color:#808030; ">,</span></span>
<span class="line_wrapper">      image<span style="color:#800080; ">:</span> <span style="color:#800000; ">'</span><span style="color:#0000e6; ">https://i.imgur.com/Sd1AgUOm.jpg</span><span style="color:#800000; ">'</span><span style="color:#808030; ">,</span></span>
<span class="line_wrapper">    <span style="color:#800080; ">}</span></span>
<span class="line_wrapper">  <span style="color:#800080; ">}</span><span style="color:#808030; ">)</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">function</span> handleNameChange<span style="color:#808030; ">(</span>e<span style="color:#808030; ">)</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">    setPerson<span style="color:#808030; ">(</span><span style="color:#800080; ">{</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span>person<span style="color:#808030; ">,</span></span>
<span class="line_wrapper">      name<span style="color:#800080; ">:</span> e<span style="color:#808030; ">.</span>target<span style="color:#808030; ">.</span>value</span>
<span class="line_wrapper">    <span style="color:#800080; ">}</span><span style="color:#808030; ">)</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper">  <span style="color:#800080; ">}</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">function</span> handleTitleChange<span style="color:#808030; ">(</span>e<span style="color:#808030; ">)</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">    setPerson<span style="color:#808030; ">(</span><span style="color:#800080; ">{</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span>person<span style="color:#808030; ">,</span></span>
<span class="line_wrapper">      artwork<span style="color:#800080; ">:</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">,</span></span>
<span class="line_wrapper">        title<span style="color:#800080; ">:</span> e<span style="color:#808030; ">.</span>target<span style="color:#808030; ">.</span>value</span>
<span class="line_wrapper">      <span style="color:#800080; ">}</span></span>
<span class="line_wrapper">    <span style="color:#800080; ">}</span><span style="color:#808030; ">)</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper">  <span style="color:#800080; ">}</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">function</span> handleCityChange<span style="color:#808030; ">(</span>e<span style="color:#808030; ">)</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">    setPerson<span style="color:#808030; ">(</span><span style="color:#800080; ">{</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span>person<span style="color:#808030; ">,</span></span>
<span class="line_wrapper">      artwork<span style="color:#800080; ">:</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">,</span></span>
<span class="line_wrapper">        city<span style="color:#800080; ">:</span> e<span style="color:#808030; ">.</span>target<span style="color:#808030; ">.</span>value</span>
<span class="line_wrapper">      <span style="color:#800080; ">}</span></span>
<span class="line_wrapper">    <span style="color:#800080; ">}</span><span style="color:#808030; ">)</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper">  <span style="color:#800080; ">}</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">function</span> handleImageChange<span style="color:#808030; ">(</span>e<span style="color:#808030; ">)</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">    setPerson<span style="color:#808030; ">(</span><span style="color:#800080; ">{</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span>person<span style="color:#808030; ">,</span></span>
<span class="line_wrapper">      artwork<span style="color:#800080; ">:</span> <span style="color:#800080; ">{</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">.</span><span style="color:#808030; ">.</span><span style="color:#808030; ">.</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">,</span></span>
<span class="line_wrapper">        image<span style="color:#800080; ">:</span> e<span style="color:#808030; ">.</span>target<span style="color:#808030; ">.</span>value</span>
<span class="line_wrapper">      <span style="color:#800080; ">}</span></span>
<span class="line_wrapper">    <span style="color:#800080; ">}</span><span style="color:#808030; ">)</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper">  <span style="color:#800080; ">}</span></span>
<span class="line_wrapper"></span>
<span class="line_wrapper">  <span style="color:#800000; font-weight:bold; ">return</span> <span style="color:#808030; ">(</span></span>
<span class="line_wrapper">    <span style="color:#808030; ">&lt;</span><span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#e34adc; ">Name:</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">&lt;</span><span style="color:#797997; ">input</span></span>
<span class="line_wrapper">          value<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>name<span style="color:#800080; ">}</span></span>
<span class="line_wrapper">          onChange<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>handleNameChange<span style="color:#800080; ">}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        </span><span style="color:#800000; ">/</span><span style="color:#0000e6; ">&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;</span><span style="color:#800000; ">/</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#e34adc; ">Title:</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">&lt;</span><span style="color:#797997; ">input</span></span>
<span class="line_wrapper">          value<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">.</span>title<span style="color:#800080; ">}</span></span>
<span class="line_wrapper">          onChange<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>handleTitleChange<span style="color:#800080; ">}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        </span><span style="color:#800000; ">/</span><span style="color:#0000e6; ">&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;</span><span style="color:#800000; ">/</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#e34adc; ">City:</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">&lt;</span><span style="color:#797997; ">input</span></span>
<span class="line_wrapper">          value<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">.</span>city<span style="color:#800080; ">}</span></span>
<span class="line_wrapper">          onChange<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>handleCityChange<span style="color:#800080; ">}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        </span><span style="color:#800000; ">/</span><span style="color:#0000e6; ">&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;</span><span style="color:#800000; ">/</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#e34adc; ">Image:</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">&lt;</span><span style="color:#797997; ">input</span></span>
<span class="line_wrapper">          value<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">.</span>image<span style="color:#800080; ">}</span></span>
<span class="line_wrapper">          onChange<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>handleImageChange<span style="color:#800080; ">}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">        </span><span style="color:#800000; ">/</span><span style="color:#0000e6; ">&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      &lt;</span><span style="color:#800000; ">/</span>label<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>p<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">&lt;</span>i<span style="color:#808030; ">&gt;</span><span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">.</span>title<span style="color:#800080; ">}</span><span style="color:#808030; ">&lt;</span><span style="color:#808030; ">/</span>i<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#800080; ">{</span><span style="color:#800000; ">'</span><span style="color:#0000e6; "> by </span><span style="color:#800000; ">'</span><span style="color:#800080; ">}</span></span>
<span class="line_wrapper">        <span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>name<span style="color:#800080; ">}</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">&lt;</span>br <span style="color:#808030; ">/</span><span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">        <span style="color:#808030; ">(</span>located <span style="color:#800000; font-weight:bold; ">in</span> <span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">.</span>city<span style="color:#800080; ">}</span><span style="color:#808030; ">)</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span><span style="color:#808030; ">/</span>p<span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">      <span style="color:#808030; ">&lt;</span>img</span>
<span class="line_wrapper">        src<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">.</span>image<span style="color:#800080; ">}</span></span>
<span class="line_wrapper">        alt<span style="color:#808030; ">=</span><span style="color:#800080; ">{</span>person<span style="color:#808030; ">.</span>artwork<span style="color:#808030; ">.</span>title<span style="color:#800080; ">}</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">      </span><span style="color:#800000; ">/</span><span style="color:#0000e6; ">&gt;</span></span>
<span class="line_wrapper"><span style="color:#0000e6; ">    &lt;</span><span style="color:#800000; ">/</span><span style="color:#808030; ">&gt;</span></span>
<span class="line_wrapper">  <span style="color:#808030; ">)</span><span style="color:#800080; ">;</span></span>
<span class="line_wrapper"><span style="color:#800080; ">}</span></span></pre>