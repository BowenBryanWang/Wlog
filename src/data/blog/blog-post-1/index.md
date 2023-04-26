---
category: "blog"
cover: "./cover.jpg"
title: "Blog Post 1"
description: "Mauris neque libero, aliquet vel mollis nec, euismod sed tellus. Mauris convallis dictum elit id volutpat."
date: "2019-11-13"
tags: ["Photography"]
published: true
---

<!DOCTYPE html>
<html lang="zh-Hans-CN">

<head>
    <link rel="stylesheet" type="text/css" href="./css/modern-norm.min.css" />
    <link rel="stylesheet" type="text/css" href="./css/prism.min.css" />
    <link rel="stylesheet" type="text/css" href="./css/katex.min.css" />
    <link rel="stylesheet" type="text/css" href="./css/wolai.css" />
</head>

<body>
    <header>
        <div class="image"></div>
        <div class="title">
            <div class="banner">
                <div class="icon"></div>
            </div>
            <div data-title="非线性方程的解法" class="main-title"></div>
        </div>
    </header>
    <article>
        <div id="m1whKkUYVMzBGhaFMgeFn4" class="wolai-block wolai-text">
            <div><span class="inline-wrap">要求解的单变量非线性方程为</span></div>
        </div>
        <div id="qmUQS4YrFyThmpqtqjfGeq" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                    <mo separator="true">,</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">f(x)=0,</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.8389em;vertical-align:-0.1944em;"></span><span
                                class="mord">0</span><span class="mpunct">,</span></span></span></span></span></div>
        <div id="6MDp3eCEWiG8As5kQUYJH3" class="wolai-block wolai-text">
            <div><span class="inline-wrap">其中, 函数 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo>:</mo>
                                        <mi mathvariant="double-struck">R</mi>
                                        <mo>→</mo>
                                        <mi mathvariant="double-struck">R</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f: \mathbb{R} \rightarrow \mathbb{R}
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">:</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6889em;"></span><span
                                    class="mord mathbb">R</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">→</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6889em;"></span><span
                                    class="mord mathbb">R</span></span></span></span></span><span
                    class="inline-wrap">。一般而言, 非线性方程的解的存在性和个数是很难确定的, 它可能无解, 也可能有一个或多个解。</span></div>
        </div>
        <div id="sFi3AzuFsAdEPytzc4xhMT" class="wolai-block wolai-text">
            <div><span class="inline-wrap">在实际问题中, 往往要求的是自变量在一定范围内的解, 如限定 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                        <mo>∈</mo>
                                        <mo stretchy="false">[</mo>
                                        <mi>a</mi>
                                        <mo separator="true">,</mo>
                                        <mi>b</mi>
                                        <mo stretchy="false">]</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x \in[a, b]</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5782em;vertical-align:-0.0391em;"></span><span
                                    class="mord mathnormal">x</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mopen">[</span><span class="mord mathnormal">a</span><span
                                    class="mpunct">,</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                    class="mclose">]</span></span></span></span></span><span class="inline-wrap"> 。函数
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                    class="mord mathnormal"
                                    style="margin-right:0.10764em;">f</span></span></span></span></span><span
                    class="inline-wrap">一般为连续函数, 可记为 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>∈</mo>
                                        <mi>C</mi>
                                        <mo stretchy="false">[</mo>
                                        <mi>a</mi>
                                        <mo separator="true">,</mo>
                                        <mi>b</mi>
                                        <mo stretchy="false">]</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x) \in C[a, b]</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.07153em;">C</span><span
                                    class="mopen">[</span><span class="mord mathnormal">a</span><span
                                    class="mpunct">,</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                    class="mclose">]</span></span></span></span></span><span class="inline-wrap">。假设在区间
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo stretchy="false">[</mo>
                                        <mi>a</mi>
                                        <mo separator="true">,</mo>
                                        <mi>b</mi>
                                        <mo stretchy="false">]</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">[a, b]</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mopen">[</span><span class="mord mathnormal">a</span><span
                                    class="mpunct">,</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                    class="mclose">]</span></span></span></span></span><span class="inline-wrap"> 上方程根为
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">, 也称 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 为函数 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">
                    的零点。</span></div>
        </div>
        <blockquote id="mnnDyhmA32zkGVitUagzkm" class="wolai-block"><span class="inline-wrap"><b>定义 2.1:
                </b></span><span class="inline-wrap">对光滑函数 </span><span><span class="katex"><span
                        class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">f</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.8889em;vertical-align:-0.1944em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span></span></span></span></span><span
                class="inline-wrap">, 若 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <msup>
                                        <mi>f</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <mo>⋯</mo>
                                    <mo>=</mo>
                                    <msup>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo stretchy="false">(</mo>
                                            <mi>m</mi>
                                            <mo>−</mo>
                                            <mn>1</mn>
                                            <mo stretchy="false">)</mo>
                                        </mrow>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                    <mo separator="true">,</mo>
                                    <mi>m</mi>
                                    <mo>&gt;</mo>
                                    <mn>1</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    f\left(x^{*}\right)=f^{\prime}\left(x^{*}\right)=\cdots=f^{(m-1)}\left(x^{*}\right)=0,
                                    m&gt;1</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1.0019em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.7519em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.3669em;"></span><span class="minner">⋯</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1.138em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.888em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mopen mtight">(</span><span
                                                                class="mord mathnormal mtight">m</span><span
                                                                class="mbin mtight">−</span><span
                                                                class="mord mtight">1</span><span
                                                                class="mclose mtight">)</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.8389em;vertical-align:-0.1944em;"></span><span
                                class="mord">0</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">m</span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">&gt;</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.6444em;"></span><span
                                class="mord">1</span></span></span></span></span><span class="inline-wrap">, 但
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo stretchy="false">(</mo>
                                            <mi>m</mi>
                                            <mo stretchy="false">)</mo>
                                        </mrow>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo mathvariant="normal">≠</mo>
                                    <mn>0</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">f^{(m)}\left(x^{*}\right) \neq 0</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.138em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.888em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mopen mtight">(</span><span
                                                                class="mord mathnormal mtight">m</span><span
                                                                class="mclose mtight">)</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span
                                        class="mord vbox"><span class="thinbox"><span class="rlap"><span class="strut"
                                                    style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                                    class="inner"><span class="mord"><span
                                                            class="mrel"></span></span></span><span
                                                    class="fix"></span></span></span></span></span><span
                                    class="mrel">=</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">0</span></span></span></span></span><span class="inline-wrap">, 则 称
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 为方程 (2.1) 的 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>m</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">m </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.4306em;"></span><span
                                class="mord mathnormal">m</span></span></span></span></span><span
                class="inline-wrap"><b>重根。</b></span><span class="inline-wrap">若 </span><span><span class="katex"><span
                        class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>m</mi>
                                    <mo>=</mo>
                                    <mn>1</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">m=1</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.4306em;"></span><span class="mord mathnormal">m</span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.6444em;"></span><span
                                class="mord">1</span></span></span></span></span><span class="inline-wrap">, 即
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                    <mo separator="true">,</mo>
                                    <msup>
                                        <mi>f</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo mathvariant="normal">≠</mo>
                                    <mn>0</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">f\left(x^{*}\right)=0,
                                    f^{\prime}\left(x^{*}\right) \neq 0</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1.0019em;vertical-align:-0.25em;"></span><span class="mord">0</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord"><span class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.7519em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span
                                        class="mord vbox"><span class="thinbox"><span class="rlap"><span class="strut"
                                                    style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                                    class="inner"><span class="mord"><span
                                                            class="mrel"></span></span></span><span
                                                    class="fix"></span></span></span></span></span><span
                                    class="mrel">=</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">0</span></span></span></span></span><span class="inline-wrap"> 时, 称
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 为单根。</span></blockquote>
        <h3 id="pNviiomNUG77PtwYgBHCLE" class="wolai-block"><span class="inline-wrap">问题敏感性</span></h3>
        <div id="55Pva29vF6opBaRUdDK79F" class="wolai-block wolai-text">
            <div><span class="inline-wrap">要分析敏感性, 首先应假设问题中的数据如何扰动, 一种易于分析的情况是将非线性方程写成</span></div>
        </div>
        <div id="d5XyBqt1GjFu8S6Q9GbBBn" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>=</mo>
                                    <mi>y</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">f(x)=y</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.625em;vertical-align:-0.1944em;"></span><span class="mord mathnormal"
                                style="margin-right:0.03588em;">y</span></span></span></span></span></div>
        <div id="bV8DbnBdoJSGt1Qe1rqXjW" class="wolai-block wolai-text">
            <div><span class="inline-wrap">的形式, 然后讨论 y 在 0 值附近的扰动造成的问题敏感性。此时, 求根问题变成了函数求值 问题</span><span><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>y</mi>
                                        <mo>=</mo>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex"> y=f(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">
                    的反问题。若函数值 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span
                    class="inline-wrap">对</span><span class="inline-wrap"><b>输入参数 </b></span><span><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.4306em;"></span><span
                                    class="mord mathnormal">x</span></span></span></span></span><span
                    class="inline-wrap"> 很不敏感 ( </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.4306em;"></span><span
                                    class="mord mathnormal">x</span></span></span></span></span><span
                    class="inline-wrap"> 在解 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 附近变化), 则 求根问题将很敏感; 反之, 若函数值对参数值很敏感, 求根则不敏感。这两种情况如图 2-1 所示。</span></div>
        </div>
        <div id="oC6fjgXaRS7x2EuMDgdAMH" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image.png" style="width: 443px" /></figure>
        </div>
        <div id="bv2SuAvXg4tDD6iqy5TfP1" class="wolai-block wolai-text">
            <div><span class="inline-wrap">下面分析 y 发生扰动 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi mathvariant="normal">Δ</mi>
                                        <mi>y</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\Delta y</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.8778em;vertical-align:-0.1944em;"></span><span
                                    class="mord">Δ</span><span class="mord mathnormal"
                                    style="margin-right:0.03588em;">y</span></span></span></span></span><span
                    class="inline-wrap"> 引起的方程的根的扰动 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi mathvariant="normal">Δ</mi>
                                        <mi>x</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\Delta x</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6833em;"></span><span class="mord">Δ</span><span
                                    class="mord mathnormal">x</span></span></span></span></span><span
                    class="inline-wrap"> 。由于当 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                        <mo>=</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x=x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.4306em;"></span><span
                                    class="mord mathnormal">x</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 时, </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>y</mi>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">y=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap">, 因此使 用绝对
                    (而不是相对) 条件数</span></div>
        </div>
        <div id="w4YmdDBpiMkzDrLyzK9p5x" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mtext> cond </mtext>
                                    <mo>=</mo>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <mfrac>
                                            <mrow>
                                                <mi mathvariant="normal">Δ</mi>
                                                <mi>x</mi>
                                            </mrow>
                                            <mrow>
                                                <mi mathvariant="normal">Δ</mi>
                                                <mi>y</mi>
                                            </mrow>
                                        </mfrac>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <mo>≈</mo>
                                    <mfrac>
                                        <mn>1</mn>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msup>
                                                <mi>f</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msup>
                                                    <mi>x</mi>
                                                    <mo lspace="0em" rspace="0em">∗</mo>
                                                </msup>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                    </mfrac>
                                </mrow>
                                <annotation encoding="application/x-tex">\text { cond }=\left|\frac{\Delta x}{\Delta
                                    y}\right| \approx \frac{1}{\left|f^{\prime}\left(x^{*}\right)\right|} </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6944em;"></span><span class="mord text"><span
                                    class="mord"> cond </span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:2.412em;vertical-align:-0.95em;"></span><span class="minner"><span
                                    class="mopen"><span class="delimsizing mult"><span class="vlist-t vlist-t2"><span
                                                class="vlist-r"><span class="vlist" style="height:1.462em;"><span
                                                        style="top:-2.266em;"><span class="pstrut"
                                                            style="height:3.216em;"></span><span
                                                            class="delimsizinginner delim-size1"><span>∣</span></span></span><span
                                                        style="top:-2.864em;"><span class="pstrut"
                                                            style="height:3.216em;"></span><span
                                                            style="height:1.216em;width:0.3333em;"><svg
                                                                xmlns="http://www.w3.org/2000/svg" width='0.3333em'
                                                                height='1.216em' style='width:0.3333em'
                                                                viewBox='0 0 333.33000000000004 1216'
                                                                preserveAspectRatio='xMinYMin'>
                                                                <path
                                                                    d='M145 0 H188 V1216 H145z M145 0 H188 V1216 H145z' />
                                                            </svg></span></span><span style="top:-4.072em;"><span
                                                            class="pstrut" style="height:3.216em;"></span><span
                                                            class="delimsizinginner delim-size1"><span>∣</span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.95em;"><span></span></span></span></span></span></span><span
                                    class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:1.3603em;"><span style="top:-2.314em;"><span
                                                            class="pstrut" style="height:3em;"></span><span
                                                            class="mord"><span class="mord">Δ</span><span
                                                                class="mord mathnormal"
                                                                style="margin-right:0.03588em;">y</span></span></span><span
                                                        style="top:-3.225em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="frac-line"
                                                            style="border-bottom-width:0.05em;"></span></span><span
                                                        style="top:-3.677em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="mord"><span
                                                                class="mord">Δ</span><span
                                                                class="mord mathnormal">x</span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.8804em;"><span></span></span></span></span></span><span
                                        class="mclose nulldelimiter"></span></span><span class="mclose"><span
                                        class="delimsizing mult"><span class="vlist-t vlist-t2"><span
                                                class="vlist-r"><span class="vlist" style="height:1.462em;"><span
                                                        style="top:-2.266em;"><span class="pstrut"
                                                            style="height:3.216em;"></span><span
                                                            class="delimsizinginner delim-size1"><span>∣</span></span></span><span
                                                        style="top:-2.864em;"><span class="pstrut"
                                                            style="height:3.216em;"></span><span
                                                            style="height:1.216em;width:0.3333em;"><svg
                                                                xmlns="http://www.w3.org/2000/svg" width='0.3333em'
                                                                height='1.216em' style='width:0.3333em'
                                                                viewBox='0 0 333.33000000000004 1216'
                                                                preserveAspectRatio='xMinYMin'>
                                                                <path
                                                                    d='M145 0 H188 V1216 H145z M145 0 H188 V1216 H145z' />
                                                            </svg></span></span><span style="top:-4.072em;"><span
                                                            class="pstrut" style="height:3.216em;"></span><span
                                                            class="delimsizinginner delim-size1"><span>∣</span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.95em;"><span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">≈</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:2.2574em;vertical-align:-0.936em;"></span><span
                                class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.3214em;"><span style="top:-2.314em;"><span
                                                        class="pstrut" style="height:3em;"></span><span
                                                        class="mord"><span class="minner"><span
                                                                class="mopen delimcenter" style="top:0em;">∣</span><span
                                                                class="mord"><span class="mord mathnormal"
                                                                    style="margin-right:0.10764em;">f</span><span
                                                                    class="msupsub"><span class="vlist-t"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.6779em;"><span
                                                                                    style="top:-2.989em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                                                class="mspace"
                                                                style="margin-right:0.1667em;"></span><span
                                                                class="minner"><span class="mopen delimcenter"
                                                                    style="top:0em;">(</span><span class="mord"><span
                                                                        class="mord mathnormal">x</span><span
                                                                        class="msupsub"><span class="vlist-t"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.6147em;"><span
                                                                                        style="top:-2.989em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                                                    class="mclose delimcenter"
                                                                    style="top:0em;">)</span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">∣</span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord">1</span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.936em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span></span></span></span></span></div>
        <div id="kCykqbUtSmp8za68qYEj9N" class="wolai-block wolai-text">
            <div><span class="inline-wrap">条件数的大小反映方程求根问题 (式 2.1 ) 的敏感程度,</span><span class="red inline-wrap">
                </span><span class="red inline-wrap"><b>若 </b></span><span class="red"><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo>∣</mo>
                                        <msup>
                                            <mi>f</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                        </mrow>
                                        <mo stretchy="false">)</mo>
                                        <mo>∣</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\mid f^{\prime}\left(x^{*}\right. ) \mid
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mrel">∣</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1.0019em;vertical-align:-0.25em;"></span><span class="mord"><span
                                        class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                        class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose nulldelimiter"></span></span><span class="mclose">)</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">∣</span></span></span></span></span><span
                    class="red inline-wrap"><b>很小, 则问题很敏感, 是 一个病态问题; 若</b></span><span class="red"><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msup>
                                            <mi>f</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex"> \left|f^{\prime}\left(x^{*}\right)\right|
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal"
                                            style="margin-right:0.10764em;">f</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7519em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.6887em;"><span
                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">∣</span></span></span></span></span></span><span
                    class="red inline-wrap"><b>很大, 则问题不敏感</b></span><span class="inline-wrap"><b>。</b></span><span
                    class="inline-wrap">一种特殊情况是 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>f</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f^{\prime}\left(x^{*}\right)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.10764em;">f</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap">,
                </span><span class="red inline-wrap">即 </span><span class="red"><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="red inline-wrap"><b> 为重根, 此时求根问题很敏感</b></span><span class="inline-wrap">, 原问题的微小扰动将造成很大的解误差,
                    甚至改变解的存在性和唯一性</span></div>
        </div>
        <div id="cXMxXDjwScLgm4M2bS3A97" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_1.png" style="width: 326px" />
            </figure>
        </div>
        <h2 id="5SNMjMyFGkYcJoNKiX3jsb" class="wolai-block"><span class="inline-wrap">二分法</span></h2>
        <div id="pE3DjxJk78dmSvWU51oXnz" class="wolai-block wolai-text">
            <div><span class="inline-wrap">首先介绍</span><span class="inline-wrap"><b>有根区间</b></span><span
                    class="inline-wrap">的概念。有根区间就是包含至少一个根的区间，它限定了根存在的范围。如果能计算出一个非常小的有根区间，那么区间的中点就是一个很好的近似解。</span></div>
        </div>
        <div id="bBTiRcxNTnToT4tBK5BXoz" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_2.png" style="width: 268px" />
            </figure>
        </div>
        <div id="ojKfQRWaa2HSeuzNzuQP1J" class="wolai-block wolai-text">
            <div><span class="inline-wrap">二分法的思想很简单, 就是每次将有根区间一分为二, 得到长度逐次减半的区间序列 </span><span><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo fence="true">{</mo>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>a</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo separator="true">,</mo>
                                            <msub>
                                                <mi>b</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo fence="true">}</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left\{\left(a_{k}, b_{k}\right)\right\}
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">{</span><span
                                        class="minner"><span class="mopen delimcenter" style="top:0em;">(</span><span
                                            class="mord"><span class="mord mathnormal">a</span><span
                                                class="msupsub"><span class="vlist-t vlist-t2"><span
                                                        class="vlist-r"><span class="vlist"
                                                            style="height:0.3361em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mathnormal mtight"
                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mpunct">,</span><span class="mspace"
                                            style="margin-right:0.1667em;"></span><span class="mord"><span
                                                class="mord mathnormal">b</span><span class="msupsub"><span
                                                    class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.3361em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mathnormal mtight"
                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">}</span></span></span></span></span></span><span
                    class="inline-wrap">, </span><span class="inline-wrap"><b>则区间中点 </b></span><span><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo>=</mo>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>a</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo>+</mo>
                                            <msub>
                                                <mi>b</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mi mathvariant="normal">/</mi>
                                        <mn>2</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k}=\left(a_{k}+b_{k}\right) / 2
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">=</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">a</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">+</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">b</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span
                                    class="mord">/2</span></span></span></span></span><span class="inline-wrap"><b>就是第 k
                        步迭代的近似解</b></span></div>
        </div>
        <div id="pvThDh3ZRHZbs3pQubwWpj" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_3.png" style="width: 520px" />
            </figure>
        </div>
        <h3 id="4onZSLqTJQGoFMN9xau3Ug" class="wolai-block"><span class="inline-wrap">误差</span></h3>
        <div id="67U4DLGry1ruWYfKMLbUWR" class="wolai-block wolai-text">
            <div><span class="inline-wrap">假设二分法得到的有根区间序列为 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">{</mo>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>a</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo separator="true">,</mo>
                                                <msub>
                                                    <mi>b</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo separator="true">,</mo>
                                            <mi>k</mi>
                                            <mo>=</mo>
                                            <mn>0</mn>
                                            <mo separator="true">,</mo>
                                            <mn>1</mn>
                                            <mo separator="true">,</mo>
                                            <mn>2</mn>
                                            <mo separator="true">,</mo>
                                            <mo>⋯</mo>
                                            <mtext> </mtext>
                                            <mo fence="true">}</mo>
                                        </mrow>
                                        <mo separator="true">,</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left\{\left(a_{k}, b_{k}\right), k=0,1,2,
                                        \cdots\right\},</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">{</span><span
                                        class="minner"><span class="mopen delimcenter" style="top:0em;">(</span><span
                                            class="mord"><span class="mord mathnormal">a</span><span
                                                class="msupsub"><span class="vlist-t vlist-t2"><span
                                                        class="vlist-r"><span class="vlist"
                                                            style="height:0.3361em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mathnormal mtight"
                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mpunct">,</span><span class="mspace"
                                            style="margin-right:0.1667em;"></span><span class="mord"><span
                                                class="mord mathnormal">b</span><span class="msupsub"><span
                                                    class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.3361em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mathnormal mtight"
                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span
                                        class="mpunct">,</span><span class="mspace"
                                        style="margin-right:0.1667em;"></span><span class="mord mathnormal"
                                        style="margin-right:0.03148em;">k</span><span class="mspace"
                                        style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                        class="mspace" style="margin-right:0.2778em;"></span><span
                                        class="mord">0</span><span class="mpunct">,</span><span class="mspace"
                                        style="margin-right:0.1667em;"></span><span class="mord">1</span><span
                                        class="mpunct">,</span><span class="mspace"
                                        style="margin-right:0.1667em;"></span><span class="mord">2</span><span
                                        class="mpunct">,</span><span class="mspace"
                                        style="margin-right:0.1667em;"></span><span class="minner">⋯</span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span
                                        class="mclose delimcenter" style="top:0em;">}</span></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span
                                    class="mpunct">,</span></span></span></span></span><span class="inline-wrap"> 若取解
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo>=</mo>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>a</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo>+</mo>
                                            <msub>
                                                <mi>b</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mi mathvariant="normal">/</mi>
                                        <mn>2</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k}=\left(a_{k}+b_{k}\right) / 2
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">=</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">a</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">+</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">b</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span
                                    class="mord">/2</span></span></span></span></span><span class="inline-wrap">,
                    则</span><span class="inline-wrap"><b>误差</b></span><span class="inline-wrap">为</span></div>
        </div>
        <div id="pEdfZMXRJFNEQdqApe16Pn" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo>−</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <mo>&lt;</mo>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>b</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>a</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mi mathvariant="normal">/</mi>
                                    <mn>2</mn>
                                    <mo>=</mo>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>b</mi>
                                            <mn>0</mn>
                                        </msub>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>a</mi>
                                            <mn>0</mn>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mi mathvariant="normal">/</mi>
                                    <msup>
                                        <mn>2</mn>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msup>
                                    <mo separator="true">,</mo>
                                    <mspace width="1em" />
                                    <mi>k</mi>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                    <mo separator="true">,</mo>
                                    <mn>1</mn>
                                    <mo separator="true">,</mo>
                                    <mn>2</mn>
                                    <mo separator="true">,</mo>
                                    <mo>⋯</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    \left|x_{k}-x^{*}\right|&lt;\left(b_{k}-a_{k}\right) / 2=\left(b_{0}-a_{0}\right) /
                                    2^{k+1}, \quad k=0,1,2, \cdots</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7387em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">b</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">a</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord">/2</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1.1491em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">b</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">0</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">a</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">0</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord">/</span><span
                                class="mord"><span class="mord">2</span><span class="msupsub"><span
                                        class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.8991em;"><span
                                                    style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span></span></span></span></span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:1em;"></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="mord mathnormal"
                                style="margin-right:0.03148em;">k</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.8389em;vertical-align:-0.1944em;"></span><span
                                class="mord">0</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord">1</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord">2</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span
                                class="minner">⋯</span></span></span></span></span></div>
        <h3 id="41dQUvGmVuRjjzzDCPczt5" class="wolai-block"><span class="inline-wrap">稳定性和准确度</span></h3>
        <div id="pwTGPXyYgNfa8w5bUuTEAQ" class="wolai-block wolai-text">
            <div><span class="inline-wrap">算法的稳定性考查的是计算过程中的误差对结果的影响。</span><span
                    class="inline-wrap"><b>对于二分法来说,主要的计算步骤是计算函数值，一般采用双精度浮点数计算函数值的误差很小</b></span><span
                    class="inline-wrap">，而其他计算是少量的加减法，因此不至于对有根区间以及最终结果的准确度造成多大影响。</span><span
                    class="red inline-wrap">另外，在计算过程中解的误差限逐次减半,这也说明二分法是稳定的。</span></div>
        </div>
        <div id="oCYh9qmAizHcBSMMPuRTL8" class="wolai-block wolai-text">
            <div><span class="inline-wrap"><b>算法稳定性：运算简单，误差逐渐缩小，比较稳定</b></span></div>
        </div>
        <aside id="4J5NAa1ypVkuZV1XBn2EfK" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理 2.2</b></span><span
                class="inline-wrap">: 在实际的浮点算术体系下采用二分法解方程</span><span><span class="katex"><span
                        class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                </mrow>
                                <annotation encoding="application/x-tex"> f(x)=0</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">0</span></span></span></span></span><span class="inline-wrap">,
                设初始有根区间为</span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mo stretchy="false">(</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex"> (a, b)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span
                                class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap">, 则：
                结果的误差限最小可达到 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mn>2</mn>
                                        <mrow>
                                            <mo fence="true">⌊</mo>
                                            <msub>
                                                <mrow>
                                                    <mi>log</mi>
                                                    <mo>⁡</mo>
                                                </mrow>
                                                <mn>2</mn>
                                            </msub>
                                            <mi mathvariant="normal">∣</mi>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mi mathvariant="normal">∣</mi>
                                            <mo fence="true">⌋</mo>
                                        </mrow>
                                    </msup>
                                    <mo>⋅</mo>
                                    <mn>2</mn>
                                    <msub>
                                        <mi>ε</mi>
                                        <mrow>
                                            <mi>m</mi>
                                            <mi>a</mi>
                                            <mi>c</mi>
                                            <mi>h</mi>
                                            <mo separator="true">,</mo>
                                        </mrow>
                                    </msub>
                                </mrow>
                                <annotation encoding="application/x-tex">2^{\left\lfloor \log_{2}|x^{*}|
                                    \right\rfloor}\cdot 2 \varepsilon_{{mach, }}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.8973em;"></span><span class="mord"><span class="mord">2</span><span
                                    class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.8973em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="minner mtight"><span
                                                                    class="mopen mtight delimcenter"
                                                                    style="top:0em;"><span
                                                                        class="mtight">⌊</span></span><span
                                                                    class="mop mtight"><span class="mop mtight"><span
                                                                            class="mtight">l</span><span
                                                                            class="mtight">o</span><span class="mtight"
                                                                            style="margin-right:0.01389em;">g</span></span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.1944em;"><span
                                                                                        style="top:-2.2341em;margin-right:0.0714em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.5em;"></span><span
                                                                                            class="sizing reset-size3 size1 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.2659em;"><span></span></span></span></span></span></span><span
                                                                    class="mspace mtight"
                                                                    style="margin-right:0.1952em;"></span><span
                                                                    class="mord mtight">∣</span><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight">x</span><span
                                                                        class="msupsub"><span class="vlist-t"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.7633em;"><span
                                                                                        style="top:-2.931em;margin-right:0.0714em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.5em;"></span><span
                                                                                            class="sizing reset-size3 size1 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                                                    class="mord mtight">∣</span><span
                                                                    class="mclose mtight delimcenter"
                                                                    style="top:0em;"><span
                                                                        class="mtight">⌋</span></span></span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">⋅</span><span
                                class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span
                                class="strut" style="height:0.9305em;vertical-align:-0.2861em;"></span><span
                                class="mord">2</span><span class="mord"><span class="mord mathnormal">ε</span><span
                                    class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                class="vlist" style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mtight"><span
                                                                    class="mord mathnormal mtight">ma</span><span
                                                                    class="mord mathnormal mtight">c</span><span
                                                                    class="mord mathnormal mtight">h</span><span
                                                                    class="mpunct mtight">,</span></span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2861em;"><span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">, 其中 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 为准确解, 对应的相对误差限为 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mn>2</mn>
                                    <msub>
                                        <mi>ε</mi>
                                        <mrow>
                                            <mi mathvariant="normal">m</mi>
                                            <mi mathvariant="normal">a</mi>
                                            <mi mathvariant="normal">c</mi>
                                            <mi mathvariant="normal">h</mi>
                                        </mrow>
                                    </msub>
                                </mrow>
                                <annotation encoding="application/x-tex">2 \varepsilon_{\mathrm{mach}} </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.7944em;vertical-align:-0.15em;"></span><span class="mord">2</span><span
                                class="mord"><span class="mord mathnormal">ε</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mtight"><span
                                                                    class="mord mathrm mtight">mach</span></span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span>
        </aside>
        <div id="vZJpeZrZiRHgd6NYPoedm1" class="wolai-block wolai-text">
            <div><span class="inline-wrap">最后,对二分法说明几点。</span></div>
        </div>
        <ul class="wolai-block">
            <li id="ummQRGfo2QpfiDqyxN3vY6">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">二分法是求单变量方程(z)=0<span
                        class="jill"></span>的实根的一种可靠算法,若存在有根区间，则一定能收敛。</span>
            </li>
            <li id="gwFufTZUt3oBJse2YkxZFK">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">二分法解的误差不一定随迭代次数增加一直减小，在实际的有限精度算术体系中，误差限存在最小值</span>
            </li>
            <li id="bCdxE3XD4D41Ln3gebpiB6">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">二分法的缺点是，有时</span><span
                    class="inline-wrap"><b>不易确定合适的初始有根区间(含两个初始值）</b></span><span class="inline-wrap">、</span><span
                    class="inline-wrap"><b>收敛较慢</b></span><span
                    class="inline-wrap">，且无法求解偶数重的根。因此,实际应用中常将二分法与其他方法结合起来。</span>
            </li>
        </ul>
        <h2 id="uqgyWQ7dm6wBnZdNMp4hzS" class="wolai-block"><span class="inline-wrap">不动点迭代法</span></h2>
        <h3 id="hBcfu5dx9q7uQMnK9nwv3F" class="wolai-block"><span class="inline-wrap">原理</span></h3>
        <div id="uTCe1R9taCiZ9wzrA3dSqB" class="wolai-block wolai-text">
            <div><span class="inline-wrap">通过某种等价变换, 可将非线性方程</span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex"> f(x)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span
                    class="inline-wrap">改写为</span></div>
        </div>
        <div id="mkZkYyhSn4cJV59BAoVyqW" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mi>x</mi>
                                    <mo>=</mo>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x=\varphi(x) </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.4306em;"></span><span class="mord mathnormal">x</span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span></div>
        <div id="bkBBN2ZpYt55q4uwUsDTHn" class="wolai-block wolai-text">
            <div><span class="inline-wrap">其中, </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>φ</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varphi(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                    class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">
                    为连续函数。给定初始值 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mn>0</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{0}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">0</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 后, 可构造迭代计 算公式</span></div>
        </div>
        <div id="4eW4eqwXWfQXrYrNQ3wawQ" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msub>
                                    <mo>=</mo>
                                    <mi>φ</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mspace width="1em" />
                                    <mo stretchy="false">(</mo>
                                    <mi>k</mi>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                    <mo separator="true">,</mo>
                                    <mn>1</mn>
                                    <mo separator="true">,</mo>
                                    <mn>2</mn>
                                    <mo separator="true">,</mo>
                                    <mo>⋯</mo>
                                    <mtext> </mtext>
                                    <mo stretchy="false">)</mo>
                                    <mspace width="1em" />
                                    <mo stretchy="false">(</mo>
                                    <mn>2.8</mn>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{k+1}=\varphi\left(x_{k}\right)
                                    \quad(k=0,1,2, \cdots) \quad(2.8)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:1em;"></span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mopen">(</span><span
                                class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord">0</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord">1</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord">2</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="minner">⋯</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mclose">)</span><span class="mspace" style="margin-right:1em;"></span><span
                                class="mopen">(</span><span class="mord">2.8</span><span
                                class="mclose">)</span></span></span></span></span></div>
        <div id="dAUjErxC546SX5bxW6oaJw" class="wolai-block wolai-text">
            <div><span class="inline-wrap">从而得到近似解序列 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo stretchy="false">{</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo stretchy="false">}</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\{x_{k}\} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mopen">{</span><span class="mord"><span class="mord mathnormal">x</span><span
                                        class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                    class="vlist" style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose">}</span></span></span></span></span><span
                    class="inline-wrap">。很容易证明若序列 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo stretchy="false">{</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo stretchy="false">}</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\{x_{k}\}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mopen">{</span><span class="mord"><span class="mord mathnormal">x</span><span
                                        class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                    class="vlist" style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose">}</span></span></span></span></span><span class="inline-wrap"> 收敛,
                    其极限必为原 方程的解 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">。由于解 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 满足 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo>=</mo>
                                        <mi>φ</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}=\varphi\left(x^{*}\right)
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">=</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal">φ</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap">, 因此称它为函数 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>φ</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varphi(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                    class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 的不动点
                    (fixed point), 此方法为求解非线性方程的不动点迭代法</span></div>
        </div>
        <div id="tkJE1GHJ9F1FDLoMCidLLT" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_4.png" style="width: 279px" />
            </figure>
        </div>
        <h3 id="iPV6ktKS2XktYVMheLHXpF" class="wolai-block"><span class="inline-wrap">全局收敛的充分条件</span></h3>
        <div id="6mymf7eXGihSLawaeRHhRq" class="wolai-block wolai-text">
            <div><span class="inline-wrap">定理<span class="jill"></span>2. 3<span
                        class="jill"></span>给出一个函数存在唯一不动点的充分条件。</span></div>
        </div>
        <aside id="rXSiowTzDwfZ2ktViEvotp" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理 2.3</b></span><span
                class="inline-wrap">: 设 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>∈</mo>
                                    <mi>C</mi>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x) \in C[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.07153em;">C</span><span class="mopen">[</span><span
                                class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">,
                若满足如下两个条件:
                (1) 对任意 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>x</mi>
                                    <mo>∈</mo>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x \in[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.5782em;vertical-align:-0.0391em;"></span><span
                                class="mord mathnormal">x</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">[</span><span
                                class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">,有
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>a</mi>
                                    <mo>⩽</mo>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>⩽</mo>
                                    <mi>b</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">a \leqslant \varphi(x) \leqslant b</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.7733em;vertical-align:-0.1367em;"></span><span
                                class="mord mathnormal">a</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.6944em;"></span><span
                                class="mord mathnormal">b</span></span></span></span></span><span class="inline-wrap"> 。
                (2) </span><span class="inline-wrap"><b>存在</b></span><span class="inline-wrap">正常数 </span><span><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>L</mi>
                                    <mo>∈</mo>
                                    <mo stretchy="false">(</mo>
                                    <mn>0</mn>
                                    <mo separator="true">,</mo>
                                    <mn>1</mn>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">L \in(0,1)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.7224em;vertical-align:-0.0391em;"></span><span
                                class="mord mathnormal">L</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">(</span><span
                                class="mord">0</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord">1</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap">, 使对任意
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>1</mn>
                                    </msub>
                                    <mo separator="true">,</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>2</mn>
                                    </msub>
                                    <mo>∈</mo>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{1}, x_{2} \in[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">2</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mopen">[</span><span class="mord mathnormal">a</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">,</span>
            <div id="ce7FHbgfVYx6zvz5r9MNip" class="wolai-block wolai-text"><span class="katex-display"><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                                display="block">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <mi>φ</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mn>1</mn>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo>−</mo>
                                            <mi>φ</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mn>2</mn>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>&lt;</mo>
                                        <mi>L</mi>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mn>1</mn>
                                            </msub>
                                            <mo>−</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mn>2</mn>
                                            </msub>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">
                                        \left|\varphi\left(x_{1}\right)-\varphi\left(x_{2}\right)\right|&lt;L\left|x_{1}-x_{2}\right|
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord mathnormal">φ</span><span class="mspace"
                                        style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.3011em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mtight">1</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span
                                        class="mord mathnormal">φ</span><span class="mspace"
                                        style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.3011em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mtight">2</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal">L</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3011em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3011em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">2</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">∣</span></span></span></span></span></span></div>
            <div id="edPxTxJxfZMkTVqZiFB1fq" class="wolai-block wolai-text">
                <div><span class="inline-wrap">则 </span><span><span class="katex"><span class="katex-mathml"><math
                                    xmlns="http://www.w3.org/1998/Math/MathML">
                                    <semantics>
                                        <mrow>
                                            <mi>φ</mi>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                        </mrow>
                                        <annotation encoding="application/x-tex">\varphi(x)</annotation>
                                    </semantics>
                                </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                        class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                        class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                        class="mord mathnormal">x</span><span
                                        class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 在
                    </span><span><span class="katex"><span class="katex-mathml"><math
                                    xmlns="http://www.w3.org/1998/Math/MathML">
                                    <semantics>
                                        <mrow>
                                            <mo stretchy="false">[</mo>
                                            <mi>a</mi>
                                            <mo separator="true">,</mo>
                                            <mi>b</mi>
                                            <mo stretchy="false">]</mo>
                                        </mrow>
                                        <annotation encoding="application/x-tex">[a, b] </annotation>
                                    </semantics>
                                </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                        class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                        class="mopen">[</span><span class="mord mathnormal">a</span><span
                                        class="mpunct">,</span><span class="mspace"
                                        style="margin-right:0.1667em;"></span><span
                                        class="mord mathnormal">b</span><span
                                        class="mclose">]</span></span></span></span></span><span
                        class="inline-wrap">上存在不动点, 且不动点是唯一的。</span></div>
            </div>
        </aside>
        <div id="eR3mCa7dTm5zgXKbK9qq6b" class="wolai-block wolai-text">
            <div><span class="inline-wrap">事实上, 通过画函数曲线图的方式也可以形象地说明不动点 的存在性,如图 2-5 所示, 在虚线正方形中曲线 </span><span><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>φ</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varphi(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                    class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">
                    必与正方形对角线相交。</span></div>
        </div>
        <div id="bm5nYZYBdXRVbiSmgDXwem" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_5.png" style="width: 522px" />
            </figure>
        </div>
        <div id="32kYyk78B21R8EUavn3DAT" class="wolai-block wolai-text">
            <div><span class="inline-wrap">定理<span class="jill"></span>2. 4<span
                        class="jill"></span>给出了不动点迭代法收敛的充分条件。</span></div>
        </div>
        <aside id="d6EpUPd58VmErwxocS1DeJ" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理 2.4:</b></span><span
                class="inline-wrap"> 设 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>∈</mo>
                                    <mi>C</mi>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x) \in C[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.07153em;">C</span><span class="mopen">[</span><span
                                class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap"> 满足定理 2.3
                的两个条件, 则对于</span><span class="red inline-wrap"><b>任意初值 </b></span><span class="red"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>0</mn>
                                    </msub>
                                    <mo>∈</mo>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{0} \in[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">0</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mopen">[</span><span class="mord mathnormal">a</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">, 由
                不动点迭代法得到的序列 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mo stretchy="false">{</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mi>k</mi>
                                    </msub>
                                    <mo stretchy="false">}</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\{x_{k}\}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mclose">}</span></span></span></span></span><span class="inline-wrap"> 收敛到
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 的不动点
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">, 并有误差估计</span>
            <div id="bwMMmfafKnKT49V3ULhhGQ" class="wolai-block wolai-text"><span class="katex-display"><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                                display="block">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo>−</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>⩽</mo>
                                        <mfrac>
                                            <msup>
                                                <mi>L</mi>
                                                <mi>k</mi>
                                            </msup>
                                            <mrow>
                                                <mn>1</mn>
                                                <mo>−</mo>
                                                <mi>L</mi>
                                            </mrow>
                                        </mfrac>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mn>1</mn>
                                            </msub>
                                            <mo>−</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mn>0</mn>
                                            </msub>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mi mathvariant="normal">.</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|x_{k}-x^{*}\right| \leqslant
                                        \frac{L^{k}}{1-L}\left|x_{1}-x_{0}\right| .</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7387em;"><span
                                                            style="top:-3.113em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:2.2954em;vertical-align:-0.7693em;"></span><span
                                    class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:1.5261em;"><span style="top:-2.314em;"><span
                                                            class="pstrut" style="height:3em;"></span><span
                                                            class="mord"><span class="mord">1</span><span class="mspace"
                                                                style="margin-right:0.2222em;"></span><span
                                                                class="mbin">−</span><span class="mspace"
                                                                style="margin-right:0.2222em;"></span><span
                                                                class="mord mathnormal">L</span></span></span><span
                                                        style="top:-3.225em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="frac-line"
                                                            style="border-bottom-width:0.05em;"></span></span><span
                                                        style="top:-3.677em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="mord"><span
                                                                class="mord"><span class="mord mathnormal">L</span><span
                                                                    class="msupsub"><span class="vlist-t"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.8491em;"><span
                                                                                    style="top:-3.063em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span></span></span></span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.7693em;"><span></span></span></span></span></span><span
                                        class="mclose nulldelimiter"></span></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3011em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3011em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">0</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span
                                    class="mord">.</span></span></span></span></span></div>
        </aside>
        <div id="gZspD5HfGYKcanhUE1aete" class="wolai-block wolai-text">
            <div><span class="inline-wrap">定理 2.4 为判断不动点迭代法的收敛性提供了依据, 这种收敛不依赖于初值 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mn>0</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{0}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">0</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 的选取, 因此称为</span><span class="inline-wrap"><b>全局收敛</b></span></div>
        </div>
        <div id="6zVTA2GK7gc8bFHGRrENtU" class="wolai-block wolai-text">
            <div><span class="inline-wrap">为了方便应用, 也可将定理 2.3 和定理 2.4 中的第二个条件替换 为: </span><span
                    class="inline-wrap"><b>对任意 </b></span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                        <mo>∈</mo>
                                        <mo stretchy="false">[</mo>
                                        <mi>a</mi>
                                        <mo separator="true">,</mo>
                                        <mi>b</mi>
                                        <mo stretchy="false">]</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x \in[a, b]</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5782em;vertical-align:-0.0391em;"></span><span
                                    class="mord mathnormal">x</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mopen">[</span><span class="mord mathnormal">a</span><span
                                    class="mpunct">,</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                    class="mclose">]</span></span></span></span></span><span class="inline-wrap"><b>, 有
                    </b></span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msup>
                                                <mi>φ</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>&lt;</mo>
                                        <mn>1</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|\varphi^{\prime}(x)\right|&lt;1
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7519em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                        class="mopen">(</span><span class="mord mathnormal">x</span><span
                                        class="mclose">)</span><span class="mclose delimcenter"
                                        style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">1</span></span></span></span></span><span class="inline-wrap"><b>,
                        得到便于使用的定理 2.5 。</b></span></div>
        </div>
        <aside id="g2itgduamWbVNBaV3KJZvh" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理 2.5</b></span><span
                class="inline-wrap">：设 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>∈</mo>
                                    <mi>C</mi>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x) \in C[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.07153em;">C</span><span class="mopen">[</span><span
                                class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">,
                且满足如下两个条件:
                (1) 对任意 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>x</mi>
                                    <mo>∈</mo>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x \in[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.5782em;vertical-align:-0.0391em;"></span><span
                                class="mord mathnormal">x</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">[</span><span
                                class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">,有
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>a</mi>
                                    <mo>⩽</mo>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>⩽</mo>
                                    <mi>b</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">a \leqslant \varphi(x) \leqslant b</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.7733em;vertical-align:-0.1367em;"></span><span
                                class="mord mathnormal">a</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.6944em;"></span><span
                                class="mord mathnormal">b</span></span></span></span></span><span class="inline-wrap"> 。
                (2) 对任意 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>x</mi>
                                    <mo>∈</mo>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x \in[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.5782em;vertical-align:-0.0391em;"></span><span
                                class="mord mathnormal">x</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">[</span><span
                                class="mord mathnormal">a</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">,有
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msup>
                                            <mi>φ</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <mo>&lt;</mo>
                                    <mn>1</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">\left|\varphi^{\prime}(x)\right|&lt;1
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.0019em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                        class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mclose delimcenter"
                                    style="top:0em;">∣</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">1</span></span></span></span></span><span class="inline-wrap"> 。
                则对于任意初值 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>0</mn>
                                    </msub>
                                    <mo>∈</mo>
                                    <mo stretchy="false">[</mo>
                                    <mi>a</mi>
                                    <mo separator="true">,</mo>
                                    <mi>b</mi>
                                    <mo stretchy="false">]</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{0} \in[a, b]</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">0</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mopen">[</span><span class="mord mathnormal">a</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord mathnormal">b</span><span
                                class="mclose">]</span></span></span></span></span><span class="inline-wrap">,
                由不动点迭代法得到的序列 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mo stretchy="false">{</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mi>k</mi>
                                    </msub>
                                    <mo stretchy="false">}</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\{x_{k}\}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mclose">}</span></span></span></span></span><span class="inline-wrap"> 收敛到
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 的不动点
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">, 并 有误差估计</span>
            <div id="wZuviX8j2nemrncNJwNaE6" class="wolai-block wolai-text"><span class="katex-display"><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                                display="block">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo>−</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>⩽</mo>
                                        <mfrac>
                                            <msup>
                                                <mi>L</mi>
                                                <mi>k</mi>
                                            </msup>
                                            <mrow>
                                                <mn>1</mn>
                                                <mo>−</mo>
                                                <mi>L</mi>
                                            </mrow>
                                        </mfrac>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mn>1</mn>
                                            </msub>
                                            <mo>−</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mn>0</mn>
                                            </msub>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo separator="true">,</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|x_{k}-x^{*}\right| \leqslant
                                        \frac{L^{k}}{1-L}\left|x_{1}-x_{0}\right|, </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7387em;"><span
                                                            style="top:-3.113em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:2.2954em;vertical-align:-0.7693em;"></span><span
                                    class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:1.5261em;"><span style="top:-2.314em;"><span
                                                            class="pstrut" style="height:3em;"></span><span
                                                            class="mord"><span class="mord">1</span><span class="mspace"
                                                                style="margin-right:0.2222em;"></span><span
                                                                class="mbin">−</span><span class="mspace"
                                                                style="margin-right:0.2222em;"></span><span
                                                                class="mord mathnormal">L</span></span></span><span
                                                        style="top:-3.225em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="frac-line"
                                                            style="border-bottom-width:0.05em;"></span></span><span
                                                        style="top:-3.677em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="mord"><span
                                                                class="mord"><span class="mord mathnormal">L</span><span
                                                                    class="msupsub"><span class="vlist-t"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.8491em;"><span
                                                                                    style="top:-3.063em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span></span></span></span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.7693em;"><span></span></span></span></span></span><span
                                        class="mclose nulldelimiter"></span></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3011em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3011em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">0</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span
                                    class="mpunct">,</span></span></span></span></span></div>
            <div id="3ELbbxPoDDMUcNcQW7P54J" class="wolai-block wolai-text">
                <div><span class="inline-wrap"><b>其中 L 是 </b></span><span><span class="katex"><span
                                class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                    <semantics>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msup>
                                                <mi>φ</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <annotation encoding="application/x-tex">\left|\varphi^{\prime}(x)\right|
                                        </annotation>
                                    </semantics>
                                </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                        class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                        class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                            class="mord"><span class="mord mathnormal">φ</span><span
                                                class="msupsub"><span class="vlist-t"><span class="vlist-r"><span
                                                            class="vlist" style="height:0.7519em;"><span
                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                            class="mopen">(</span><span class="mord mathnormal">x</span><span
                                            class="mclose">)</span><span class="mclose delimcenter"
                                            style="top:0em;">∣</span></span></span></span></span></span><span
                        class="inline-wrap"><b> 的最大值。</b></span></div>
            </div>
        </aside>
        <h3 id="uvSY1rDq1h8WnMwpfDb7Ss" class="wolai-block"><span class="inline-wrap">局部收敛性</span></h3>
        <blockquote id="5ArnJ6e9WWb4AvXExyDmyn" class="wolai-block"><span class="inline-wrap"><b>定义 2.2:
                </b></span><span class="inline-wrap">设函数 </span><span><span class="katex"><span
                        class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 存在不动点
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">, </span><span class="red inline-wrap"><b>若存在 </b></span><span class="red"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="red inline-wrap"><b> 的某个邻域 </b></span><span class="red"><span class="katex"><span
                        class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>D</mi>
                                    <mo>:</mo>
                                    <mrow>
                                        <mo fence="true">[</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo>−</mo>
                                        <mi>δ</mi>
                                        <mo separator="true">,</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo>+</mo>
                                        <mi>δ</mi>
                                        <mo fence="true">]</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">D:\left[x^{*}-\delta, x^{*}+\delta\right]
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6833em;"></span><span class="mord mathnormal"
                                style="margin-right:0.02778em;">D</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">:</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">[</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord mathnormal"
                                    style="margin-right:0.03785em;">δ</span><span class="mpunct">,</span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">+</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord mathnormal"
                                    style="margin-right:0.03785em;">δ</span><span class="mclose delimcenter"
                                    style="top:0em;">]</span></span></span></span></span></span><span
                class="inline-wrap">, 对于任意初值 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>0</mn>
                                    </msub>
                                    <mo>∈</mo>
                                    <mi>D</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{0} \in D</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6891em;vertical-align:-0.15em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">0</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.6833em;"></span><span class="mord mathnormal"
                                style="margin-right:0.02778em;">D</span></span></span></span></span><span
                class="inline-wrap">, 迭代法 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msub>
                                    <mo>=</mo>
                                    <mi>φ</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{k+1}=\varphi\left(x_{k}\right)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter"
                                    style="top:0em;">)</span></span></span></span></span></span><span
                class="inline-wrap"> 产生的解序列 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mo stretchy="false">{</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mi>k</mi>
                                    </msub>
                                    <mo stretchy="false">}</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\{x_{k}\} </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mclose">}</span></span></span></span></span><span class="inline-wrap">收敛到
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">, 则称</span><span class="inline-wrap"><b>迭代法局部收敛</b></span><span
                class="inline-wrap">。</span></blockquote>
        <aside id="puYqNWdE1nJsG15pn4SuYq" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理 2.6:</b></span><span
                class="inline-wrap"> 设 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*} </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">为函数 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 的不动点,
                若</span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>φ</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex"> \varphi^{\prime}(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.0019em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal">φ</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.7519em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mopen">(</span><span class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 在
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 的某个邻域上连续, 且 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msup>
                                            <mi>φ</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <mo>&lt;</mo>
                                    <mn>1</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    \left|\varphi^{\prime}\left(x^{*}\right)\right|&lt;1</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.0019em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                        class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span
                                    class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">1</span></span></span></span></span><span class="inline-wrap">, 则不动点迭代法
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msub>
                                    <mo>=</mo>
                                    <mi>φ</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{k+1}=\varphi\left(x_{k}\right)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter"
                                    style="top:0em;">)</span></span></span></span></span></span><span
                class="inline-wrap"> 局部收敛。</span>
        </aside>
        <div id="ip8rWRekPb5C3MtUnUPFhS" class="wolai-block wolai-text">
            <div><span class="inline-wrap">注意:</span></div>
        </div>
        <ul class="wolai-block">
            <li id="jz5tw8XzzcHU8XrYLUu35o">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">只需看 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>φ</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varphi^{\prime}\left(x^{*}\right)
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap"> ，因此局部收敛易判断</span>
            </li>
            <li id="qa4uE8KgTvBCEdX7ngCGCu">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap"> </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msup>
                                                <mi>φ</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msup>
                                                    <mi>x</mi>
                                                    <mo lspace="0em" rspace="0em">∗</mo>
                                                </msup>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>&lt;</mo>
                                        <mn>1</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">
                                        \left|\varphi^{\prime}\left(x^{*}\right)\right|&lt;1</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7519em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.6887em;"><span
                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">&lt;</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">1</span></span></span></span></span><span class="inline-wrap"> 是充分条件,
                    某种程度上有一定的必要性. 因为若 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msup>
                                                <mi>g</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msup>
                                                    <mi>x</mi>
                                                    <mo lspace="0em" rspace="0em">∗</mo>
                                                </msup>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>&gt;</mo>
                                        <mn>1</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">
                                        \left|g^{\prime}\left(x^{*}\right)\right|&gt;1</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal"
                                            style="margin-right:0.03588em;">g</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7519em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.6887em;"><span
                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">&gt;</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">1</span></span></span></span></span><span class="inline-wrap">, 则在
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">附近局部 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msup>
                                                <mi>g</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>&gt;</mo>
                                        <mn>1</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|g^{\prime}(x)\right|&gt;1
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal"
                                            style="margin-right:0.03588em;">g</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7519em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                        class="mopen">(</span><span class="mord mathnormal">x</span><span
                                        class="mclose">)</span><span class="mclose delimcenter"
                                        style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">&gt;</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">1</span></span></span></span></span><span class="inline-wrap">.</span>
            </li>
        </ul>
        <div id="qyYj8rygaLsWL4ATr1pbLk" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                        <mo>−</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mrow></mrow>
                                        </msup>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <mi>g</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo>−</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mrow></mrow>
                                        </msup>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msup>
                                            <mi>g</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mo stretchy="false">(</mo>
                                        <mi>ξ</mi>
                                        <mo stretchy="false">)</mo>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo>−</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mrow></mrow>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <mo>&gt;</mo>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo>−</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mrow></mrow>
                                        </msup>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    \left|x_{k+1}-x^{}\right|=\left|g\left(x_{k}\right)-x^{}\right|=\left|g^{\prime}(\xi)\left(x_{k}-x^{}\right)\right|&gt;\left|x_{k}-x^{}\right|
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">+</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.413em;"><span
                                                        style="top:-2.413em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">∣</span><span class="mord mathnormal"
                                    style="margin-right:0.03588em;">g</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.413em;"><span
                                                        style="top:-2.413em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1.0519em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                        class="mord mathnormal" style="margin-right:0.03588em;">g</span><span
                                        class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.8019em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal"
                                    style="margin-right:0.04601em;">ξ</span><span class="mclose">)</span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.413em;"><span
                                                            style="top:-2.413em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span
                                    class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">&gt;</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.413em;"><span
                                                        style="top:-2.413em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter"
                                    style="top:0em;">∣</span></span></span></span></span></span></div>
        <div id="azUyg24N9PRKuCyaSTtSdq" class="wolai-block wolai-text">
            <div><span class="inline-wrap">误差有放大的趋势</span></div>
        </div>
        <div id="6ELoyt7syC8WcdPPneK2GV" class="wolai-block wolai-text">
            <div><span><span class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msup>
                                                <mi>g</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msup>
                                                    <mi>x</mi>
                                                    <mo lspace="0em" rspace="0em">∗</mo>
                                                </msup>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>=</mo>
                                        <mn>1</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|g^{\prime}\left(x^{*}\right)\right|=1
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal"
                                            style="margin-right:0.03588em;">g</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7519em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.6887em;"><span
                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">1</span></span></span></span></span><span class="inline-wrap"> 的例子:
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                        <mo>=</mo>
                                        <mi>b</mi>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k+1}=b-x_{k}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">+</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">=</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:0.7778em;vertical-align:-0.0833em;"></span><span
                                    class="mord mathnormal">b</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                    class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 不收敛
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                        <mo>=</mo>
                                        <mfrac>
                                            <msubsup>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                                <mn>3</mn>
                                            </msubsup>
                                            <mn>3</mn>
                                        </mfrac>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k+1}=\frac{x_{k}^{3}}{3}-x_{k}
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">+</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">=</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1.4941em;vertical-align:-0.345em;"></span><span class="mord"><span
                                        class="mopen nulldelimiter"></span><span class="mfrac"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:1.1491em;"><span style="top:-2.655em;"><span
                                                            class="pstrut" style="height:3em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">3</span></span></span></span><span
                                                        style="top:-3.225em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="frac-line"
                                                            style="border-bottom-width:0.05em;"></span></span><span
                                                        style="top:-3.5252em;"><span class="pstrut"
                                                            style="height:3em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mtight"><span
                                                                        class="mord mathnormal mtight">x</span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.8913em;"><span
                                                                                        style="top:-2.214em;margin-left:0em;margin-right:0.0714em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.5em;"></span><span
                                                                                            class="sizing reset-size3 size1 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mathnormal mtight"
                                                                                                    style="margin-right:0.03148em;">k</span></span></span></span><span
                                                                                        style="top:-2.931em;margin-right:0.0714em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.5em;"></span><span
                                                                                            class="sizing reset-size3 size1 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">3</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.286em;"><span></span></span></span></span></span></span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.345em;"><span></span></span></span></span></span><span
                                        class="mclose nulldelimiter"></span></span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                    class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 收敛 (在 0 附近的区间上）</span></div>
        </div>
        <h3 id="mkJNH7Z7CYths6jywrJ5Rp" class="wolai-block"><span class="inline-wrap">稳定性与收敛阶</span></h3>
        <div id="r7DE112zLamdjGvyvufPix" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_6.png" style="width: 100%" />
            </figure>
        </div>
        <blockquote id="7yKZfrfJQCkyrMXnAsAL5F" class="bg-blond wolai-block"><span class="inline-wrap"><b>定义
                    2.3</b></span><span class="inline-wrap">：设一个迭代解序列 </span><span><span class="katex"><span
                        class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mo stretchy="false">{</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>0</mn>
                                    </msub>
                                    <mo separator="true">,</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>1</mn>
                                    </msub>
                                    <mo separator="true">,</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>2</mn>
                                    </msub>
                                    <mo separator="true">,</mo>
                                    <mo>⋯</mo>
                                    <mtext> </mtext>
                                    <mo separator="true">,</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mi>k</mi>
                                    </msub>
                                    <mo>⋯</mo>
                                    <mtext> </mtext>
                                    <mo stretchy="false">}</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\{x_{0}, x_{1}, x_{2}, \cdots, x_{k} \cdots\}
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mopen">{</span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">0</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">2</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="minner">⋯</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="mpunct">,</span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner">⋯</span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mclose">}</span></span></span></span></span><span class="inline-wrap"> 收敛于准确解
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">, 若迭代解的误差 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>e</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mi>k</mi>
                                    </msub>
                                    <mo>−</mo>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                    <mo separator="true">,</mo>
                                    <mi>k</mi>
                                    <mo>=</mo>
                                    <mn>1</mn>
                                    <mo separator="true">,</mo>
                                    <mn>2</mn>
                                    <mo separator="true">,</mo>
                                    <mo>⋯</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">e\left(x_{k}\right)=x_{k}-x^{*}, k=1,2, \cdots
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">e</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.7333em;vertical-align:-0.15em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span
                                class="strut" style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord mathnormal" style="margin-right:0.03148em;">k</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.8389em;vertical-align:-0.1944em;"></span><span
                                class="mord">1</span><span class="mpunct">,</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord">2</span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="minner">⋯</span></span></span></span></span><span class="inline-wrap">
                满足以下渐近关系：</span>
            <div id="q2SFYqoDv7E9rLpAvQB4sS" class="wolai-block wolai-text"><span class="katex-display"><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                                display="block">
                                <semantics>
                                    <mrow>
                                        <munder>
                                            <mrow>
                                                <mi>lim</mi>
                                                <mo>⁡</mo>
                                            </mrow>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>→</mo>
                                                <mi mathvariant="normal">∞</mi>
                                            </mrow>
                                        </munder>
                                        <mfrac>
                                            <mrow>
                                                <mo fence="true">∣</mo>
                                                <mi>e</mi>
                                                <mrow>
                                                    <mo fence="true">(</mo>
                                                    <msub>
                                                        <mi>x</mi>
                                                        <mrow>
                                                            <mi>k</mi>
                                                            <mo>+</mo>
                                                            <mn>1</mn>
                                                        </mrow>
                                                    </msub>
                                                    <mo fence="true">)</mo>
                                                </mrow>
                                                <mo fence="true">∣</mo>
                                            </mrow>
                                            <msup>
                                                <mrow>
                                                    <mo fence="true">∣</mo>
                                                    <mi>e</mi>
                                                    <mrow>
                                                        <mo fence="true">(</mo>
                                                        <msub>
                                                            <mi>x</mi>
                                                            <mi>k</mi>
                                                        </msub>
                                                        <mo fence="true">)</mo>
                                                    </mrow>
                                                    <mo fence="true">∣</mo>
                                                </mrow>
                                                <mi>p</mi>
                                            </msup>
                                        </mfrac>
                                        <mo>=</mo>
                                        <mi>c</mi>
                                        <mo separator="true">,</mo>
                                        <mspace width="1em" />
                                        <mo stretchy="false">(</mo>
                                        <mi>c</mi>
                                        <mo mathvariant="normal">≠</mo>
                                        <mn>0</mn>
                                        <mo stretchy="false">)</mo>
                                        <mo separator="true">,</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\lim_{k \rightarrow \infty}
                                        \frac{\left|e\left(x_{k+1}\right)\right|}{\left|e\left(x_{k}\right)\right|^{p}}=c,
                                        \quad(c \neq 0),</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:2.4063em;vertical-align:-0.9793em;"></span><span
                                    class="mop op-limits"><span class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                class="vlist" style="height:0.6944em;"><span
                                                    style="top:-2.3479em;margin-left:0em;"><span class="pstrut"
                                                        style="height:3em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mrel mtight">→</span><span
                                                                class="mord mtight">∞</span></span></span></span><span
                                                    style="top:-3em;"><span class="pstrut"
                                                        style="height:3em;"></span><span><span
                                                            class="mop">lim</span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.7521em;"><span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span
                                        class="mopen nulldelimiter"></span><span class="mfrac"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:1.427em;"><span style="top:-2.2707em;"><span
                                                            class="pstrut" style="height:3em;"></span><span
                                                            class="mord"><span class="minner"><span class="minner"><span
                                                                        class="mopen delimcenter"
                                                                        style="top:0em;">∣</span><span
                                                                        class="mord mathnormal">e</span><span
                                                                        class="mspace"
                                                                        style="margin-right:0.1667em;"></span><span
                                                                        class="minner"><span class="mopen delimcenter"
                                                                            style="top:0em;">(</span><span
                                                                            class="mord"><span
                                                                                class="mord mathnormal">x</span><span
                                                                                class="msupsub"><span
                                                                                    class="vlist-t vlist-t2"><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.3361em;"><span
                                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                                    class="pstrut"
                                                                                                    style="height:2.7em;"></span><span
                                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                                        class="mord mtight"><span
                                                                                                            class="mord mathnormal mtight"
                                                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                            class="vlist-s">​</span></span><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                            class="mclose delimcenter"
                                                                            style="top:0em;">)</span></span><span
                                                                        class="mclose delimcenter"
                                                                        style="top:0em;">∣</span></span><span
                                                                    class="msupsub"><span class="vlist-t"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.8043em;"><span
                                                                                    style="top:-3.2029em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight">p</span></span></span></span></span></span></span></span></span></span></span><span
                                                        style="top:-3.225em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="frac-line"
                                                            style="border-bottom-width:0.05em;"></span></span><span
                                                        style="top:-3.677em;"><span class="pstrut"
                                                            style="height:3em;"></span><span class="mord"><span
                                                                class="minner"><span class="mopen delimcenter"
                                                                    style="top:0em;">∣</span><span
                                                                    class="mord mathnormal">e</span><span class="mspace"
                                                                    style="margin-right:0.1667em;"></span><span
                                                                    class="minner"><span class="mopen delimcenter"
                                                                        style="top:0em;">(</span><span
                                                                        class="mord"><span
                                                                            class="mord mathnormal">x</span><span
                                                                            class="msupsub"><span
                                                                                class="vlist-t vlist-t2"><span
                                                                                    class="vlist-r"><span class="vlist"
                                                                                        style="height:0.3361em;"><span
                                                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                                class="pstrut"
                                                                                                style="height:2.7em;"></span><span
                                                                                                class="sizing reset-size6 size3 mtight"><span
                                                                                                    class="mord mtight"><span
                                                                                                        class="mord mathnormal mtight"
                                                                                                        style="margin-right:0.03148em;">k</span><span
                                                                                                        class="mbin mtight">+</span><span
                                                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                                                        class="vlist-s">​</span></span><span
                                                                                    class="vlist-r"><span class="vlist"
                                                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                        class="mclose delimcenter"
                                                                        style="top:0em;">)</span></span><span
                                                                    class="mclose delimcenter"
                                                                    style="top:0em;">∣</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.9793em;"><span></span></span></span></span></span><span
                                        class="mclose nulldelimiter"></span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal">c</span><span class="mpunct">,</span><span class="mspace"
                                    style="margin-right:1em;"></span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="mopen">(</span><span
                                    class="mord mathnormal">c</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span
                                            class="mord vbox"><span class="thinbox"><span class="rlap"><span
                                                        class="strut"
                                                        style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                                        class="inner"><span class="mord"><span
                                                                class="mrel"></span></span></span><span
                                                        class="fix"></span></span></span></span></span><span
                                        class="mrel">=</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1em;vertical-align:-0.25em;"></span><span class="mord">0</span><span
                                    class="mclose">)</span><span class="mpunct">,</span></span></span></span></span>
            </div>
            <div id="7R648BzyNeJcp4pEQVADNe" class="wolai-block wolai-text">
                <div><span class="inline-wrap">则称</span><span class="inline-wrap"><b>迭代过程是 </b></span><span><span
                            class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                    <semantics>
                                        <mrow>
                                            <mi>p</mi>
                                        </mrow>
                                        <annotation encoding="application/x-tex">p</annotation>
                                    </semantics>
                                </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                        class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                        class="mord mathnormal">p</span></span></span></span></span><span
                        class="inline-wrap"><b> 阶收敛的, 或称收敛阶为 </b></span><span><span class="katex"><span
                                class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                    <semantics>
                                        <mrow>
                                            <mi>p</mi>
                                        </mrow>
                                        <annotation encoding="application/x-tex">p</annotation>
                                    </semantics>
                                </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                        class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                        class="mord mathnormal">p</span></span></span></span></span><span
                        class="inline-wrap"><b> </b></span></div>
            </div>
        </blockquote>
        <div id="m3dJQQfrubq5D1FQPn9e91" class="wolai-block wolai-text">
            <div><span class="inline-wrap">关于这个定义要注意的是，</span><span class="red inline-wrap"><u>对一个迭代法，其收敛阶<span
                            class="jill"></span>p<span class="jill"></span>的值是唯一的，若取其他值，会使极限值<span
                            class="jill"></span>c<span class="jill"></span>为<span class="jill"></span>0<span
                            class="jill"></span>或无穷大</u></span><span
                    class="inline-wrap">。此外,这个定义也适合于非线性方程求解以外的其他送代过程。</span></div>
        </div>
        <div id="b2BV3DL7YUE5WodJxJA9Wf" class="bg-blond wolai-block wolai-text wolai-center">
            <div><span class="inline-wrap"><b>对于二分法来说，它大体上具有<span class="jill"></span>1<span
                            class="jill"></span>阶收敛性，收敛常数<span class="jill"></span>c=0.5</b></span><span
                    class="inline-wrap">。</span></div>
        </div>
        <aside id="w1oC4UM68qodHC3BacyG1M" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理 2. 7</b></span><span
                class="inline-wrap">：对于不动点迭代法 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msub>
                                    <mo>=</mo>
                                    <mi>φ</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{k+1}=\varphi\left(x_{k}\right)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter"
                                    style="top:0em;">)</span></span></span></span></span></span><span
                class="inline-wrap">, 若在所求根 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 的邻域上函数 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>φ</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span
                                class="mord mathnormal">φ</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 的
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>p</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">p</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                class="mord mathnormal">p</span></span></span></span></span><span class="inline-wrap">
                阶导数 连续, </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>p</mi>
                                    <mo>⩾</mo>
                                    <mn>2</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">p \geqslant 2</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.8311em;vertical-align:-0.1944em;"></span><span
                                class="mord mathnormal">p</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩾</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.6444em;"></span><span
                                class="mord">2</span></span></span></span></span><span class="inline-wrap">, 则该迭代法在
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 的邻域上</span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>p</mi>
                                </mrow>
                                <annotation encoding="application/x-tex"> p</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                class="mord mathnormal">p</span></span></span></span></span><span
                class="inline-wrap"><b> 阶收敛</b></span><span class="inline-wrap">的充分必要条件是:</span>
            <div id="81oPEaGyTGnDjvKUAkxChW" class="wolai-block wolai-text"><span class="katex-display"><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                                display="block">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>φ</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo>=</mo>
                                        <msup>
                                            <mi>φ</mi>
                                            <mrow>
                                                <mo mathvariant="normal">′</mo>
                                                <mo mathvariant="normal">′</mo>
                                            </mrow>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo>=</mo>
                                        <mo>⋯</mo>
                                        <mo>=</mo>
                                        <msup>
                                            <mi>φ</mi>
                                            <mrow>
                                                <mo stretchy="false">(</mo>
                                                <mi>p</mi>
                                                <mo>−</mo>
                                                <mn>1</mn>
                                                <mo stretchy="false">)</mo>
                                            </mrow>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                        <mo separator="true">,</mo>
                                        <mtext>且</mtext>
                                        <msup>
                                            <mi>φ</mi>
                                            <mrow>
                                                <mo stretchy="false">(</mo>
                                                <mi>p</mi>
                                                <mo stretchy="false">)</mo>
                                            </mrow>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo mathvariant="normal">≠</mo>
                                        <mn>0</mn>
                                        <mtext>。</mtext>
                                    </mrow>
                                    <annotation encoding="application/x-tex">
                                        \varphi^{\prime}\left(x^{*}\right)=\varphi^{\prime
                                        \prime}\left(x^{*}\right)=\cdots= \varphi^{(p-1)}\left(x^{*}\right)=0, 且
                                        \varphi^{(p)}\left(x^{*}\right) \neq 0 。</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0519em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.8019em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7387em;"><span
                                                            style="top:-3.113em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1.0519em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.8019em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7387em;"><span
                                                            style="top:-3.113em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.3669em;"></span><span class="minner">⋯</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">=</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1.188em;vertical-align:-0.25em;"></span><span class="mord"><span
                                        class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.938em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mopen mtight">(</span><span
                                                                    class="mord mathnormal mtight">p</span><span
                                                                    class="mbin mtight">−</span><span
                                                                    class="mord mtight">1</span><span
                                                                    class="mclose mtight">)</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7387em;"><span
                                                            style="top:-3.113em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1.188em;vertical-align:-0.25em;"></span><span
                                    class="mord">0</span><span class="mpunct">,</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="mord cjk_fallback">且</span><span
                                    class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.938em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mopen mtight">(</span><span
                                                                    class="mord mathnormal mtight">p</span><span
                                                                    class="mclose mtight">)</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.7387em;"><span
                                                            style="top:-3.113em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span
                                            class="mord vbox"><span class="thinbox"><span class="rlap"><span
                                                        class="strut"
                                                        style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                                        class="inner"><span class="mord"><span
                                                                class="mrel"></span></span></span><span
                                                        class="fix"></span></span></span></span></span><span
                                        class="mrel">=</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:0.6833em;"></span><span class="mord">0</span><span
                                    class="mord cjk_fallback">。</span></span></span></span></span></div>
        </aside>
        <h2 id="mSCsv8VgAvZi1efdZzJonC" class="wolai-block"><span class="inline-wrap">牛顿法</span></h2>
        <div id="uS8m3xATEGUVAeKRUKapk" class="wolai-block wolai-text">
            <div><span class="inline-wrap">下面结合介绍牛顿法的构造思想。图中显示函数</span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">要求方程
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap"> 的根
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">, 即求该曲线与横坐标轴的交点。假设已得到第 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>k</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">k</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6944em;"></span><span class="mord mathnormal"
                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                    class="inline-wrap"> 个近似解 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">, 则可用如下方法得到下 一个近似解 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k+1}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">+</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> (希望它更接近</span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex"> x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> )</span></div>
        </div>
        <div id="vJByJT5FUKpuSQrewV2CEt" class="wolai-block wolai-text">
            <div><span class="inline-wrap">先求出 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 在
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                        <mo>=</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x=x_{k}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.4306em;"></span><span
                                    class="mord mathnormal">x</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 处的切线, 设切线方程为 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>y</mi>
                                        <mo>=</mo>
                                        <mi>P</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">y=P(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.13889em;">P</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">,
                    它是一次多项式函数, 用 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>P</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">P(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.13889em;">P</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 近似
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">, 则
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>P</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">P(x)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.13889em;">P</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap">
                    的根就是新的近似解 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k+1}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">+</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 从几何的角度看, 就是将切线与横轴交点处的 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.4306em;"></span><span
                                    class="mord mathnormal">x</span></span></span></span></span><span
                    class="inline-wrap">值作为下 一步近似解。</span></div>
        </div>
        <div id="vqysMZLmHNrSz9QSnGTeKd" class="wolai-block wolai-text">
            <div><span class="inline-wrap">采用点斜式公式, 切线方程为</span></div>
        </div>
        <div id="rwoiCkAA2iMN1XHGuecDDs" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mi>P</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>=</mo>
                                    <mi>f</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>+</mo>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <mi>x</mi>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <msup>
                                        <mi>f</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">P(x)=f\left(x_{k}\right)+\left(x-x_{k}\right)
                                    f^{\prime}\left(x_{k}\right) </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.13889em;">P</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace"
                                style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut"
                                style="height:1.0519em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span
                                    class="mord mathnormal">x</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="mord"><span class="mord mathnormal"
                                    style="margin-right:0.10764em;">f</span><span class="msupsub"><span
                                        class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.8019em;"><span
                                                    style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter"
                                    style="top:0em;">)</span></span></span></span></span></span></div>
        <div id="475z8VXD8aaqKm1TnxR4Ej" class="wolai-block wolai-text">
            <div><span class="inline-wrap">解方程 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>P</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">P(x)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.13889em;">P</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span
                    class="inline-wrap">,得到</span></div>
        </div>
        <div id="cQ3GiQsh3ZXSn8ypqbgyAA" class="bg-blond wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msub>
                                    <mo>=</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mi>k</mi>
                                    </msub>
                                    <mo>−</mo>
                                    <mfrac>
                                        <mrow>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                        <mrow>
                                            <msup>
                                                <mi>f</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                    </mfrac>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    x_{k+1}=x_{k}-\frac{f\left(x_{k}\right)}{f^{\prime}\left(x_{k}\right)} </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.7333em;vertical-align:-0.15em;"></span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span
                                class="strut" style="height:2.363em;vertical-align:-0.936em;"></span><span
                                class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.427em;"><span style="top:-2.314em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord"><span class="mord mathnormal"
                                                                style="margin-right:0.10764em;">f</span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.6779em;"><span
                                                                                style="top:-2.989em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                                            class="mspace" style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.936em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span></span></span></span></span></div>
        <div id="dtWvwcnTgd7H2ZH5HQ9YH8" class="wolai-block wolai-text">
            <div><span class="inline-wrap">便是牛顿迭代法的迭代计算公式。</span></div>
        </div>
        <div id="dEKE7kqaS67tPECxz8ARmc" class="wolai-block wolai-text">
            <div><span class="inline-wrap">下面考查牛顿迭代法的</span><span class="inline-wrap"><b>局部收敛性</b></span><span
                    class="inline-wrap">和</span><span class="inline-wrap"><b>收敛阶</b></span><span class="inline-wrap">。假设
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>f</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo mathvariant="normal">≠</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f^{\prime}\left(x^{*}\right) \neq 0
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.10764em;">f</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span
                                            class="mord vbox"><span class="thinbox"><span class="rlap"><span
                                                        class="strut"
                                                        style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                                        class="inner"><span class="mord"><span
                                                                class="mrel"></span></span></span><span
                                                        class="fix"></span></span></span></span></span><span
                                        class="mrel">=</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap">, 即
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 为方程 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap"> 的单根
                    (根据定义 2.1), 我们来看 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>φ</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varphi^{\prime}\left(x^{*}\right)
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap"> 的值。</span></div>
        </div>
        <div id="bJGmGMGu7tp1b2mq79VP1h" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>φ</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>=</mo>
                                    <mn>1</mn>
                                    <mo>−</mo>
                                    <mfrac>
                                        <mrow>
                                            <msup>
                                                <mrow>
                                                    <mo fence="true">[</mo>
                                                    <msup>
                                                        <mi>f</mi>
                                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                                    </msup>
                                                    <mo stretchy="false">(</mo>
                                                    <mi>x</mi>
                                                    <mo stretchy="false">)</mo>
                                                    <mo fence="true">]</mo>
                                                </mrow>
                                                <mn>2</mn>
                                            </msup>
                                            <mo>−</mo>
                                            <mi>f</mi>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                            <msup>
                                                <mi>f</mi>
                                                <mrow>
                                                    <mo mathvariant="normal">′</mo>
                                                    <mo mathvariant="normal">′</mo>
                                                </mrow>
                                            </msup>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                        </mrow>
                                        <msup>
                                            <mrow>
                                                <mo fence="true">[</mo>
                                                <msup>
                                                    <mi>f</mi>
                                                    <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                                </msup>
                                                <mo stretchy="false">(</mo>
                                                <mi>x</mi>
                                                <mo stretchy="false">)</mo>
                                                <mo fence="true">]</mo>
                                            </mrow>
                                            <mn>2</mn>
                                        </msup>
                                    </mfrac>
                                    <mo>=</mo>
                                    <mfrac>
                                        <mrow>
                                            <mi>f</mi>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                            <msup>
                                                <mi>f</mi>
                                                <mrow>
                                                    <mo mathvariant="normal">′</mo>
                                                    <mo mathvariant="normal">′</mo>
                                                </mrow>
                                            </msup>
                                            <mo stretchy="false">(</mo>
                                            <mi>x</mi>
                                            <mo stretchy="false">)</mo>
                                        </mrow>
                                        <msup>
                                            <mrow>
                                                <mo fence="true">[</mo>
                                                <msup>
                                                    <mi>f</mi>
                                                    <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                                </msup>
                                                <mo stretchy="false">(</mo>
                                                <mi>x</mi>
                                                <mo stretchy="false">)</mo>
                                                <mo fence="true">]</mo>
                                            </mrow>
                                            <mn>2</mn>
                                        </msup>
                                    </mfrac>
                                    <mo>⇒</mo>
                                    <msup>
                                        <mi>φ</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    \varphi^{\prime}(x)=1-\frac{\left[f^{\prime}(x)\right]^{2}-f(x) f^{\prime
                                    \prime}(x)}{\left[f^{\prime}(x)\right]^{2}}=\frac{f(x) f^{\prime
                                    \prime}(x)}{\left[f^{\prime}(x)\right]^{2}} \Rightarrow
                                    \varphi^{\prime}\left(x^{*}\right)=0 </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.0519em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal">φ</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.8019em;"><span
                                                    style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mopen">(</span><span class="mord mathnormal">x</span><span
                                class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span
                                class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.7278em;vertical-align:-0.0833em;"></span><span
                                class="mord">1</span><span class="mspace" style="margin-right:0.2222em;"></span><span
                                class="mbin">−</span><span class="mspace"
                                style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut"
                                style="height:2.7619em;vertical-align:-1.129em;"></span><span class="mord"><span
                                    class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.6329em;"><span style="top:-2.121em;"><span
                                                        class="pstrut" style="height:3em;"></span><span
                                                        class="mord"><span class="minner"><span class="minner"><span
                                                                    class="mopen delimcenter"
                                                                    style="top:0em;">[</span><span class="mord"><span
                                                                        class="mord mathnormal"
                                                                        style="margin-right:0.10764em;">f</span><span
                                                                        class="msupsub"><span class="vlist-t"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.6779em;"><span
                                                                                        style="top:-2.989em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                                                    class="mopen">(</span><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="mclose">)</span><span
                                                                    class="mclose delimcenter"
                                                                    style="top:0em;">]</span></span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.954em;"><span
                                                                                style="top:-3.2029em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="minner"><span class="minner"><span
                                                                    class="mopen delimcenter"
                                                                    style="top:0em;">[</span><span class="mord"><span
                                                                        class="mord mathnormal"
                                                                        style="margin-right:0.10764em;">f</span><span
                                                                        class="msupsub"><span class="vlist-t"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.7519em;"><span
                                                                                        style="top:-3.063em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                                                    class="mopen">(</span><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="mclose">)</span><span
                                                                    class="mclose delimcenter"
                                                                    style="top:0em;">]</span></span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.9559em;"><span
                                                                                style="top:-3.2048em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">2</span></span></span></span></span></span></span></span></span><span
                                                            class="mspace" style="margin-right:0.2222em;"></span><span
                                                            class="mbin">−</span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span
                                                            class="mopen">(</span><span
                                                            class="mord mathnormal">x</span><span
                                                            class="mclose">)</span><span class="mord"><span
                                                                class="mord mathnormal"
                                                                style="margin-right:0.10764em;">f</span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.7519em;"><span
                                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">′′</span></span></span></span></span></span></span></span></span><span
                                                            class="mopen">(</span><span
                                                            class="mord mathnormal">x</span><span
                                                            class="mclose">)</span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:1.129em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:2.5579em;vertical-align:-1.129em;"></span><span class="mord"><span
                                    class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.4289em;"><span style="top:-2.121em;"><span
                                                        class="pstrut" style="height:3em;"></span><span
                                                        class="mord"><span class="minner"><span class="minner"><span
                                                                    class="mopen delimcenter"
                                                                    style="top:0em;">[</span><span class="mord"><span
                                                                        class="mord mathnormal"
                                                                        style="margin-right:0.10764em;">f</span><span
                                                                        class="msupsub"><span class="vlist-t"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.6779em;"><span
                                                                                        style="top:-2.989em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                                                    class="mopen">(</span><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="mclose">)</span><span
                                                                    class="mclose delimcenter"
                                                                    style="top:0em;">]</span></span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.954em;"><span
                                                                                style="top:-3.2029em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">2</span></span></span></span></span></span></span></span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span
                                                            class="mopen">(</span><span
                                                            class="mord mathnormal">x</span><span
                                                            class="mclose">)</span><span class="mord"><span
                                                                class="mord mathnormal"
                                                                style="margin-right:0.10764em;">f</span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.7519em;"><span
                                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">′′</span></span></span></span></span></span></span></span></span><span
                                                            class="mopen">(</span><span
                                                            class="mord mathnormal">x</span><span
                                                            class="mclose">)</span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:1.129em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">⇒</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1.0519em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal">φ</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.8019em;"><span
                                                    style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7387em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span class="mord">0</span></span></span></span></span>
        </div>
        <div id="5v1zB4k5ZVMVn5ZXKvtdfL" class="wolai-block wolai-text">
            <div><span class="inline-wrap">对 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>φ</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varphi^{\prime}(x) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span
                    class="inline-wrap">再求导一次,整理公式得到（从一次导可以看出局部收敛）</span></div>
        </div>
        <div id="jdp1wQRiuujRdgdgLobsqJ" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>φ</mi>
                                        <mrow>
                                            <mo mathvariant="normal">′</mo>
                                            <mo mathvariant="normal">′</mo>
                                        </mrow>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>=</mo>
                                    <mfrac>
                                        <mrow>
                                            <msup>
                                                <mi>f</mi>
                                                <mrow>
                                                    <mo mathvariant="normal">′</mo>
                                                    <mo mathvariant="normal">′</mo>
                                                </mrow>
                                            </msup>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msup>
                                                    <mi>x</mi>
                                                    <mo lspace="0em" rspace="0em">∗</mo>
                                                </msup>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                        <mrow>
                                            <msup>
                                                <mi>f</mi>
                                                <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                            </msup>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msup>
                                                    <mi>x</mi>
                                                    <mo lspace="0em" rspace="0em">∗</mo>
                                                </msup>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                    </mfrac>
                                </mrow>
                                <annotation encoding="application/x-tex">\varphi^{\prime
                                    \prime}\left(x^{*}\right)=\frac{f^{\prime
                                    \prime}\left(x^{*}\right)}{f^{\prime}\left(x^{*}\right)}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.0519em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal">φ</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.8019em;"><span
                                                    style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′′</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7387em;"><span
                                                        style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:2.3649em;vertical-align:-0.936em;"></span><span class="mord"><span
                                    class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.4289em;"><span style="top:-2.314em;"><span
                                                        class="pstrut" style="height:3em;"></span><span
                                                        class="mord"><span class="mord"><span class="mord mathnormal"
                                                                style="margin-right:0.10764em;">f</span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.6779em;"><span
                                                                                style="top:-2.989em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                                            class="mspace" style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.6147em;"><span
                                                                                    style="top:-2.989em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord"><span class="mord mathnormal"
                                                                style="margin-right:0.10764em;">f</span><span
                                                                class="msupsub"><span class="vlist-t"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.7519em;"><span
                                                                                style="top:-3.063em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mtight">′′</span></span></span></span></span></span></span></span></span><span
                                                            class="mspace" style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.6887em;"><span
                                                                                    style="top:-3.063em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.936em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span></span></span></span></span></div>
        <div id="jg7GC445x3TLRJ6dXSeXCx" class="wolai-block wolai-text">
            <div><span class="inline-wrap">一般情况下, </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>φ</mi>
                                            <mrow>
                                                <mo mathvariant="normal">′</mo>
                                                <mo mathvariant="normal">′</mo>
                                            </mrow>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo mathvariant="normal">≠</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varphi^{\prime \prime}\left(x^{*}\right)
                                        \neq 0 </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal">φ</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel"><span class="mrel"><span
                                            class="mord vbox"><span class="thinbox"><span class="rlap"><span
                                                        class="strut"
                                                        style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                                        class="inner"><span class="mord"><span
                                                                class="mrel"></span></span></span><span
                                                        class="fix"></span></span></span></span></span><span
                                        class="mrel">=</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap">。根据定理 2.6
                    和定理 2.7 , 得到如下关于牛顿迭代法收敛性的结论。</span></div>
        </div>
        <aside id="3iKmA94Qe6y1NzTwkr1jE1" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理<span class="jill"></span>2.9
                </b></span><span class="inline-wrap">设 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 是方程 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>=</mo>
                                    <mn>0</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">f(x)=0</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span class="mclose">)</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">0</span></span></span></span></span><span class="inline-wrap">
                的单根，且</span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex"> f(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 在
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*} </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">附近有连续的二阶导数，则</span><span class="inline-wrap"><b>牛顿法至少局部二阶收敛.</b></span>
        </aside>
        <aside id="dq437qY8u2gP5phYuMSQSx" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap">若要求二阶收敛的结果，则考虑对</span><span><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msub>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{k+1}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2083em;"><span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">进行泰勒展开</span>
        </aside>
        <div id="rck6JBudYtcYhjFhPRMV3Y" class="wolai-block wolai-text">
            <div><span class="inline-wrap">方程</span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span
                    class="inline-wrap">有重根的情况</span></div>
        </div>
        <ul class="wolai-block">
            <li id="f7u3rJsar4DEmo2ysZoZzH">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">结论是只有线性阶的收敛速度</span>
            </li>
            <li id="drac5ZXWoxGywGtafG75Ma">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">并不比二分法(若可行)更好</span>
            </li>
        </ul>
        <h3 id="aNvr4PsoESkHzjcRkTdi4B" class="wolai-block"><span class="inline-wrap">判停准则</span></h3>
        <div id="2oBZjtz5J8VemnqU3i52pi" class="wolai-block wolai-text">
            <div><span class="inline-wrap">在迭代方法的实现中, 使用合适的判停准则非常重要。它既影响迭代步数, 即整体计算 效率, 也影响结果的猚确度。</span></div>
        </div>
        <div id="2ToVc4oTjdvnVQEJwM8opn" class="wolai-block wolai-text">
            <div><span class="inline-wrap">对于二分法, 我们可方便地计算结果的误差限, 根据有根区间 的长度, 就可以确定迭代过程停止的条件。而对于一般的不动点迭代法 (包括牛顿法),
                    较难直接估计误差限, 迭代过程的判停准则主要有 3 种。</span></div>
        </div>
        <ul class="wolai-block">
            <li id="rZwMEhZmBwVogWWwx6kxKH">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">残差判据, 即要求</span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>⩽</mo>
                                        <msub>
                                            <mi>ε</mi>
                                            <mn>1</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex"> \left|f\left(x_{k}\right)\right| \leqslant
                                        \varepsilon_{1}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.3361em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mathnormal mtight"
                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">ε</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">, 其中 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>ε</mi>
                                            <mn>1</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varepsilon_{1} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">ε</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">为某个阈值。</span>
            </li>
            <li id="3hQSbvdz5iVNjTyhh9UWNu">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">误差判据, 即要求 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>+</mo>
                                                    <mn>1</mn>
                                                </mrow>
                                            </msub>
                                            <mo>−</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>⩽</mo>
                                        <msub>
                                            <mi>ε</mi>
                                            <mn>2</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|x_{k+1}-x_{k}\right| \leqslant
                                        \varepsilon_{2}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">+</span><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">ε</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">, 其中 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>ε</mi>
                                            <mn>2</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varepsilon_{2} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">ε</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">为某个阈值。</span>
            </li>
            <li id="tf2r46S5bRYht4ckKoeayX">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">相对误差判据, 即要求 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>+</mo>
                                                    <mn>1</mn>
                                                </mrow>
                                            </msub>
                                            <mo>−</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                        <mo>⩽</mo>
                                        <msub>
                                            <mi>ε</mi>
                                            <mn>3</mn>
                                        </msub>
                                        <mrow>
                                            <mo fence="true">∣</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>+</mo>
                                                    <mn>1</mn>
                                                </mrow>
                                            </msub>
                                            <mo fence="true">∣</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|x_{k+1}-x_{k}\right| \leqslant
                                        \varepsilon_{3}\left|x_{k+1}\right|</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">+</span><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter" style="top:0em;">∣</span></span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel amsrm">⩽</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal">ε</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">3</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">∣</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">+</span><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">∣</span></span></span></span></span></span><span
                    class="inline-wrap">, 其中 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>ε</mi>
                                            <mn>3</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\varepsilon_{3} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">ε</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">3</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">为某个阈值。</span>
            </li>
        </ul>
        <div id="iZodSAQk3LJTA1G3Q5nSrf" class="wolai-block wolai-text">
            <div><span class="inline-wrap">残差判据和误差判据都有一定道理, 但也有缺陷。</span></div>
        </div>
        <ul class="wolai-block">
            <li id="maznbLVV98aSdXEiA21kzF">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">当问题比较敏感时 (如求重根或 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>f</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msup>
                                                <mi>x</mi>
                                                <mo lspace="0em" rspace="0em">∗</mo>
                                            </msup>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f^{\prime}\left(x^{*}\right) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.10764em;">f</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap">很小的情况 ),</span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|f\left(x_{k}\right)\right|
                                    </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                        class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                            class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                                class="mord mathnormal">x</span><span class="msupsub"><span
                                                    class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                            style="height:0.3361em;"><span
                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                    class="pstrut" style="height:2.7em;"></span><span
                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                        class="mord mtight"><span
                                                                            class="mord mathnormal mtight"
                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                            class="vlist-s">​</span></span><span class="vlist-r"><span
                                                            class="vlist"
                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                            class="mclose delimcenter" style="top:0em;">)</span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">∣</span></span></span></span></span></span><span
                    class="inline-wrap">很小并不意味着 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">很接近 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">。</span>
            </li>
            <li id="sDgwUpPqhUzcgAFsAtsEMk">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">而当近似解序列 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo stretchy="false">{</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo stretchy="false">}</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\{x_{k}\} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mopen">{</span><span class="mord"><span class="mord mathnormal">x</span><span
                                        class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                    class="vlist" style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose">}</span></span></span></span></span><span class="inline-wrap">收敛很慢时,
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">\left|x_{k+1}-x_{k}\right| </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">+</span><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">∣</span></span></span></span></span></span><span
                    class="inline-wrap">很小并不能说明</span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mo fence="true">∣</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                        <mo>−</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo fence="true">∣</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex"> \left|x_{k+1}-x^{*}\right| </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="minner"><span class="mopen delimcenter" style="top:0em;">∣</span><span
                                        class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">+</span><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mspace" style="margin-right:0.2222em;"></span><span
                                        class="mbin">−</span><span class="mspace"
                                        style="margin-right:0.2222em;"></span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.6887em;"><span
                                                            style="top:-3.063em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">∣</span></span></span></span></span></span><span
                    class="inline-wrap">很小。</span>
            </li>
        </ul>
        <div id="mLLEPwqhhE3DVgkEhuoJu8" class="wolai-block wolai-text">
            <div><span class="inline-wrap">因此, 实际应用时往往将这 3 种判据组合起来使用,有时也需要根据问题特点和经验额外设置条件。</span></div>
        </div>
        <h3 id="cQ1s5MjjYTRNc9aJBgWv2W" class="wolai-block"><span class="inline-wrap">牛顿法的问题</span></h3>
        <div id="2UgP22KEshjGkbGeEmw9L1" class="wolai-block wolai-text">
            <div><span class="inline-wrap">当 f(x) 满足 2 阶导数连续, 且 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{*}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap"> 为它的单根时,牛顿法在局部范围内 2 次收敛。然 而, 当这些假设不满足时, 牛顿法可能变得非常不可靠。若 </span><span><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 不具有连续的
                    2 阶导数, 或 者初始解不够靠近准确解, 那么它可能收敛得很慢, 或者根本不收敛。</span></div>
        </div>
        <div id="uinEnZD6CGvArcNzrJeo1v" class="wolai-block wolai-text">
            <div><span class="inline-wrap">可见, 牛顿法仍有如下 3 方面不足之处。</span></div>
        </div>
        <ul class="wolai-block">
            <li id="n19rsJHwHJszjyZD2jHuoR">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">无法保证全局收敛性。也就是说,如果初始 解 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mn>0</mn>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{0} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">0</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">不在局部收敛的范围内, 迭代过程可能发散。</span>
            </li>
            <li id="6hZBkUga1iWXLDRQw2p5kf">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">对函数的连续性要求较高,需要 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f(x) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">在
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x^{* } </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6887em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">附近有连续的 2 阶导数。</span>
            </li>
            <li id="s3Lz2m3qgAAcDjJCQr8oVY">
                <div class="marker"><svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor"
                        xmlns="http://www.w3.org/2000/svg">
                        <path d="M12 14.5a2.5 2.5 0 100-5 2.5 2.5 0 000 5z"></path>
                    </svg></div><span class="inline-wrap">每步迭代都要计算 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mn>1</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">1</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">1</span></span></span></span></span><span class="inline-wrap"> 阶导数
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msup>
                                            <mi>f</mi>
                                            <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                        </msup>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f^{\prime}(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1.0019em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.10764em;">f</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.7519em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">,
                    其计算量可能较大, 或根本无法计算。</span>
            </li>
        </ul>
        <h2 id="4kGAyyuE5s1KxGBWwpwJJ5" class="wolai-block"><span class="inline-wrap">割线法与抛物线法</span></h2>
        <div id="8WSf3FVTtyYceFFksnw9bp" class="wolai-block wolai-text">
            <div><span class="inline-wrap">割线法的基本思路就是利用差商近似导数，从而避免复杂的求导计算，利用相邻两次迭代的函数值做差商,得</span></div>
        </div>
        <div id="fAJsvsohka88Gso9ZqZBvM" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>f</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>≈</mo>
                                    <mfrac>
                                        <mrow>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo>−</mo>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mrow>
                                                        <mi>k</mi>
                                                        <mo>−</mo>
                                                        <mn>1</mn>
                                                    </mrow>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                        <mrow>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo>−</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>−</mo>
                                                    <mn>1</mn>
                                                </mrow>
                                            </msub>
                                        </mrow>
                                    </mfrac>
                                    <mi mathvariant="normal">.</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">f^{\prime}\left(x_{k}\right) \approx
                                    \frac{f\left(x_{k}\right)-f\left(x_{k-1}\right)}{x_{k}-x_{k-1}} .</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.0519em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.8019em;"><span
                                                    style="top:-3.113em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">≈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:2.3213em;vertical-align:-0.8943em;"></span><span class="mord"><span
                                    class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.427em;"><span style="top:-2.314em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord"><span class="mord mathnormal">x</span><span
                                                                class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.3361em;"><span
                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mathnormal mtight"
                                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                            class="vlist-s">​</span></span><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                            class="mspace" style="margin-right:0.2222em;"></span><span
                                                            class="mbin">−</span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mord"><span class="mord mathnormal">x</span><span
                                                                class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.3361em;"><span
                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mathnormal mtight"
                                                                                            style="margin-right:0.03148em;">k</span><span
                                                                                            class="mbin mtight">−</span><span
                                                                                            class="mord mtight">1</span></span></span></span></span><span
                                                                            class="vlist-s">​</span></span><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.2083em;"><span></span></span></span></span></span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mbin">−</span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span><span
                                                                                                class="mbin mtight">−</span><span
                                                                                                class="mord mtight">1</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.8943em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span><span
                                class="mord">.</span></span></span></span></span></div>
        <div id="iLNQWbbRkQcTUg5ziWh9N7" class="wolai-block wolai-text">
            <div><span class="inline-wrap">这在几何图形上就是函数曲线的割线,那么割线与横轴的交点就是下一个近似解,如图 2-9 所示。割线方程为</span></div>
        </div>
        <div id="h94EAmJ1Nub6MrqM8qJibT" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>P</mi>
                                        <mn>1</mn>
                                    </msub>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo>=</mo>
                                    <mi>f</mi>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mo>+</mo>
                                    <mfrac>
                                        <mrow>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo>−</mo>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mrow>
                                                        <mi>k</mi>
                                                        <mo>−</mo>
                                                        <mn>1</mn>
                                                    </mrow>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                        <mrow>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo>−</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>−</mo>
                                                    <mn>1</mn>
                                                </mrow>
                                            </msub>
                                        </mrow>
                                    </mfrac>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <mi>x</mi>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                    <mi mathvariant="normal">.</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    P_{1}(x)=f\left(x_{k}\right)+\frac{f\left(x_{k}\right)-f\left(x_{k-1}\right)}{x_{k}-x_{k-1}}\left(x-x_{k}\right)
                                    .</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal" style="margin-right:0.13889em;">P</span><span
                                    class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                class="vlist" style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mopen">(</span><span class="mord mathnormal">x</span><span
                                class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span
                                class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.2222em;"></span><span class="mbin">+</span><span class="mspace"
                                style="margin-right:0.2222em;"></span></span><span class="base"><span class="strut"
                                style="height:2.3213em;vertical-align:-0.8943em;"></span><span class="mord"><span
                                    class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.427em;"><span style="top:-2.314em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord"><span class="mord mathnormal">x</span><span
                                                                class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.3361em;"><span
                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mathnormal mtight"
                                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                            class="vlist-s">​</span></span><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                            class="mspace" style="margin-right:0.2222em;"></span><span
                                                            class="mbin">−</span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mord"><span class="mord mathnormal">x</span><span
                                                                class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.3361em;"><span
                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:2.7em;"></span><span
                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                        class="mord mtight"><span
                                                                                            class="mord mathnormal mtight"
                                                                                            style="margin-right:0.03148em;">k</span><span
                                                                                            class="mbin mtight">−</span><span
                                                                                            class="mord mtight">1</span></span></span></span></span><span
                                                                            class="vlist-s">​</span></span><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.2083em;"><span></span></span></span></span></span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mbin">−</span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span><span
                                                                                                class="mbin mtight">−</span><span
                                                                                                class="mord mtight">1</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.8943em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span
                                    class="mord mathnormal">x</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter" style="top:0em;">)</span></span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span
                                class="mord">.</span></span></span></span></span></div>
        <div id="jmbtXECzKG4jRSmZc2XaQH" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_7.png" style="width: 263px" />
            </figure>
        </div>
        <div id="oJDAsVARUYaW6YDbQc9rFv" class="wolai-block wolai-text">
            <div><span class="inline-wrap">求解方程 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>P</mi>
                                            <mn>1</mn>
                                        </msub>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">P_{1}(x)=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.13889em;">P</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap">,
                    得到下一个近似解</span></div>
        </div>
        <div id="iVW4euyjRBTJJMeTwUTqzG" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mrow>
                                            <mi>k</mi>
                                            <mo>+</mo>
                                            <mn>1</mn>
                                        </mrow>
                                    </msub>
                                    <mo>=</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mi>k</mi>
                                    </msub>
                                    <mo>−</mo>
                                    <mfrac>
                                        <mrow>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                        <mrow>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mi>k</mi>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                            <mo>−</mo>
                                            <mi>f</mi>
                                            <mrow>
                                                <mo fence="true">(</mo>
                                                <msub>
                                                    <mi>x</mi>
                                                    <mrow>
                                                        <mi>k</mi>
                                                        <mo>−</mo>
                                                        <mn>1</mn>
                                                    </mrow>
                                                </msub>
                                                <mo fence="true">)</mo>
                                            </mrow>
                                        </mrow>
                                    </mfrac>
                                    <mrow>
                                        <mo fence="true">(</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                        <mo>−</mo>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>−</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                        <mo fence="true">)</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    x_{k+1}=x_{k}-\frac{f\left(x_{k}\right)}{f\left(x_{k}\right)-f\left(x_{k-1}\right)}\left(x_{k}-x_{k-1}\right)
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6389em;vertical-align:-0.2083em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.7333em;vertical-align:-0.15em;"></span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3361em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mathnormal mtight"
                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2222em;"></span><span class="mbin">−</span><span
                                class="mspace" style="margin-right:0.2222em;"></span></span><span class="base"><span
                                class="strut" style="height:2.363em;vertical-align:-0.936em;"></span><span
                                class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.427em;"><span style="top:-2.314em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mbin">−</span><span class="mspace"
                                                            style="margin-right:0.2222em;"></span><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span><span
                                                                                                class="mbin mtight">−</span><span
                                                                                                class="mord mtight">1</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.677em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="mord"><span
                                                            class="mord mathnormal"
                                                            style="margin-right:0.10764em;">f</span><span class="mspace"
                                                            style="margin-right:0.1667em;"></span><span
                                                            class="minner"><span class="mopen delimcenter"
                                                                style="top:0em;">(</span><span class="mord"><span
                                                                    class="mord mathnormal">x</span><span
                                                                    class="msupsub"><span class="vlist-t vlist-t2"><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.3361em;"><span
                                                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                        class="pstrut"
                                                                                        style="height:2.7em;"></span><span
                                                                                        class="sizing reset-size6 size3 mtight"><span
                                                                                            class="mord mtight"><span
                                                                                                class="mord mathnormal mtight"
                                                                                                style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                class="vlist-s">​</span></span><span
                                                                            class="vlist-r"><span class="vlist"
                                                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                class="mclose delimcenter"
                                                                style="top:0em;">)</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.936em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span><span class="mspace"
                                style="margin-right:0.1667em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">−</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                    class="mclose delimcenter"
                                    style="top:0em;">)</span></span></span></span></span></span></div>
        <aside id="ew6uv6N4M8zWdi967Q7WpJ" class="bg-blond wolai-block">
            <div data-symbol="⭕" class="icon"></div><span class="inline-wrap"><b>定理 2.10</b></span><span
                class="inline-wrap">: 假设 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>f</mi>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                </mrow>
                                <annotation encoding="application/x-tex">f(x)</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="mord mathnormal"
                                style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span
                                class="mord mathnormal">x</span><span
                                class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 在根
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap"> 的邻域 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>D</mi>
                                    <mo>:</mo>
                                    <mrow>
                                        <mo fence="true">[</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo>−</mo>
                                        <mi>δ</mi>
                                        <mo separator="true">,</mo>
                                        <msup>
                                            <mi>x</mi>
                                            <mo lspace="0em" rspace="0em">∗</mo>
                                        </msup>
                                        <mo>+</mo>
                                        <mi>δ</mi>
                                        <mo fence="true">]</mo>
                                    </mrow>
                                </mrow>
                                <annotation encoding="application/x-tex">D:\left[x^{*}-\delta, x^{*}+\delta\right]
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6833em;"></span><span class="mord mathnormal"
                                style="margin-right:0.02778em;">D</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">:</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1em;vertical-align:-0.25em;"></span><span class="minner"><span
                                    class="mopen delimcenter" style="top:0em;">[</span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">−</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord mathnormal"
                                    style="margin-right:0.03785em;">δ</span><span class="mpunct">,</span><span
                                    class="mspace" style="margin-right:0.1667em;"></span><span class="mord"><span
                                        class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.6887em;"><span
                                                        style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                            style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">∗</span></span></span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2222em;"></span><span
                                    class="mbin">+</span><span class="mspace"
                                    style="margin-right:0.2222em;"></span><span class="mord mathnormal"
                                    style="margin-right:0.03785em;">δ</span><span class="mclose delimcenter"
                                    style="top:0em;">]</span></span></span></span></span></span><span
                class="inline-wrap">内具有 2 阶连续导数, </span><span class="inline-wrap"><b>且对任意 </b></span><span><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>x</mi>
                                    <mo>∈</mo>
                                    <mi>D</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">x \in D</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.5782em;vertical-align:-0.0391em;"></span><span
                                class="mord mathnormal">x</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6833em;"></span><span class="mord mathnormal"
                                style="margin-right:0.02778em;">D</span></span></span></span></span><span
                class="inline-wrap"><b>, 都有</b></span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>f</mi>
                                        <mo mathvariant="normal" lspace="0em" rspace="0em">′</mo>
                                    </msup>
                                    <mo stretchy="false">(</mo>
                                    <mi>x</mi>
                                    <mo stretchy="false">)</mo>
                                    <mo mathvariant="normal">≠</mo>
                                    <mn>0</mn>
                                </mrow>
                                <annotation encoding="application/x-tex"> f^{\prime}(x) \neq 0</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:1.0019em;vertical-align:-0.25em;"></span><span class="mord"><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist"
                                                style="height:0.7519em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">′</span></span></span></span></span></span></span></span></span><span
                                class="mopen">(</span><span class="mord mathnormal">x</span><span
                                class="mclose">)</span><span class="mspace" style="margin-right:0.2778em;"></span><span
                                class="mrel"><span class="mrel"><span class="mord vbox"><span class="thinbox"><span
                                                class="rlap"><span class="strut"
                                                    style="height:0.8889em;vertical-align:-0.1944em;"></span><span
                                                    class="inner"><span class="mord"><span
                                                            class="mrel"></span></span></span><span
                                                    class="fix"></span></span></span></span></span><span
                                    class="mrel">=</span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">0</span></span></span></span></span><span class="inline-wrap">, 如果初值
            </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>0</mn>
                                    </msub>
                                    <mo separator="true">,</mo>
                                    <msub>
                                        <mi>x</mi>
                                        <mn>1</mn>
                                    </msub>
                                    <mo>∈</mo>
                                    <mi>D</mi>
                                </mrow>
                                <annotation encoding="application/x-tex">x_{0}, x_{1} \in D</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.7335em;vertical-align:-0.1944em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">0</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mpunct">,</span><span class="mspace" style="margin-right:0.1667em;"></span><span
                                class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:0.3011em;"><span
                                                    style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                        class="pstrut" style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">1</span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.15em;"><span></span></span></span></span></span></span><span
                                class="mspace" style="margin-right:0.2778em;"></span><span class="mrel">∈</span><span
                                class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                class="strut" style="height:0.6833em;"></span><span class="mord mathnormal"
                                style="margin-right:0.02778em;">D</span></span></span></span></span><span
                class="inline-wrap"> 充分接近 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <msup>
                                        <mi>x</mi>
                                        <mo lspace="0em" rspace="0em">∗</mo>
                                    </msup>
                                </mrow>
                                <annotation encoding="application/x-tex">x^{*}</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.6887em;"></span><span class="mord"><span
                                    class="mord mathnormal">x</span><span class="msupsub"><span class="vlist-t"><span
                                            class="vlist-r"><span class="vlist" style="height:0.6887em;"><span
                                                    style="top:-3.063em;margin-right:0.05em;"><span class="pstrut"
                                                        style="height:2.7em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">∗</span></span></span></span></span></span></span></span></span></span></span></span></span><span
                class="inline-wrap">, 则割线法将按阶 </span><span><span class="katex"><span class="katex-mathml"><math
                            xmlns="http://www.w3.org/1998/Math/MathML">
                            <semantics>
                                <mrow>
                                    <mi>p</mi>
                                    <mo>=</mo>
                                    <mfrac>
                                        <mrow>
                                            <mn>1</mn>
                                            <mo>+</mo>
                                            <msqrt>
                                                <mn>5</mn>
                                            </msqrt>
                                        </mrow>
                                        <mn>2</mn>
                                    </mfrac>
                                    <mo>≈</mo>
                                    <mn>1.618</mn>
                                </mrow>
                                <annotation encoding="application/x-tex">p=\frac{1+\sqrt{5}}{2} \approx 1.618
                                </annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                class="mord mathnormal">p</span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">=</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:1.412em;vertical-align:-0.345em;"></span><span class="mord"><span
                                    class="mopen nulldelimiter"></span><span class="mfrac"><span
                                        class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                style="height:1.067em;"><span style="top:-2.655em;"><span class="pstrut"
                                                        style="height:3em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span
                                                                class="mord mtight">2</span></span></span></span><span
                                                    style="top:-3.225em;"><span class="pstrut"
                                                        style="height:3em;"></span><span class="frac-line"
                                                        style="border-bottom-width:0.05em;"></span></span><span
                                                    style="top:-3.414em;"><span class="pstrut"
                                                        style="height:3em;"></span><span
                                                        class="sizing reset-size6 size3 mtight"><span
                                                            class="mord mtight"><span class="mord mtight">1</span><span
                                                                class="mbin mtight">+</span><span
                                                                class="mord sqrt mtight"><span
                                                                    class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                                            class="vlist" style="height:0.9328em;"><span
                                                                                class="svg-align"
                                                                                style="top:-3.01em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:3.01em;"></span><span
                                                                                    class="mord mtight"
                                                                                    style="padding-left:0.833em;"><span
                                                                                        class="mord mtight">5</span></span></span><span
                                                                                style="top:-2.8828em;"><span
                                                                                    class="pstrut"
                                                                                    style="height:3.01em;"></span><span
                                                                                    class="hide-tail mtight"
                                                                                    style="min-width:0.853em;height:1.09em;"><svg
                                                                                        xmlns="http://www.w3.org/2000/svg"
                                                                                        width='400em' height='1.09em'
                                                                                        viewBox='0 0 400000 1090'
                                                                                        preserveAspectRatio='xMinYMin slice'>
                                                                                        <path d='M95,712
c-2.7,0,-7.17,-2.7,-13.5,-8c-5.8,-5.3,-9.5,-10,-9.5,-14
c0,-2,0.3,-3.3,1,-4c1.3,-2.7,23.83,-20.7,67.5,-54
c44.2,-33.3,65.8,-50.3,66.5,-51c1.3,-1.3,3,-2,5,-2c4.7,0,8.7,3.3,12,10
s173,378,173,378c0.7,0,35.3,-71,104,-213c68.7,-142,137.5,-285,206.5,-429
c69,-144,104.5,-217.7,106.5,-221
l4.819277108433735 -10.000000000000002
c5.3,-9.3,12,-14,20,-14
H400000v50H845.2724
s-225.272,467,-225.272,467s-235,486,-235,486c-2.7,4.7,-9,7,-19,7
c-6,0,-10,-1,-12,-3s-194,-422,-194,-422s-65,47,-65,47z
M844 80h400000v50h-400000z' />
                                                                                    </svg></span></span></span><span
                                                                            class="vlist-s">​</span></span><span
                                                                        class="vlist-r"><span class="vlist"
                                                                            style="height:0.1272em;"><span></span></span></span></span></span></span></span></span></span><span
                                                class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist"
                                                style="height:0.345em;"><span></span></span></span></span></span><span
                                    class="mclose nulldelimiter"></span></span><span class="mspace"
                                style="margin-right:0.2778em;"></span><span class="mrel">≈</span><span class="mspace"
                                style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                style="height:0.6444em;"></span><span
                                class="mord">1.618</span></span></span></span></span><span class="inline-wrap">
                收敛。</span>
        </aside>
        <h3 id="eRSsLmgYmfMw6ZynmpwRvP" class="wolai-block"><span class="inline-wrap">抛物线法</span></h3>
        <div id="imerhmXG45zD8KfdH8xs51" class="wolai-block wolai-text">
            <div><span class="inline-wrap">割线法使用前两个近似解得到下一个解, 将此思路进行扩展, 可考虑利用前 3 个近似解。 一般地, 前 3 个解 </span><span><span
                        class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>−</mo>
                                                <mn>2</mn>
                                            </mrow>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k-2} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">−</span><span
                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">、 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>−</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k-1} </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">−</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">和</span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mi>k</mi>
                                        </msub>
                                    </mrow>
                                    <annotation encoding="application/x-tex"> x_{k}</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.5806em;vertical-align:-0.15em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span></span></span></span></span><span
                    class="inline-wrap">, 及其对应的函数值 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>−</mo>
                                                    <mn>2</mn>
                                                </mrow>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f\left(x_{k-2}\right) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">−</span><span
                                                                        class="mord mtight">2</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap">、 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>−</mo>
                                                    <mn>1</mn>
                                                </mrow>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f\left(x_{k-1}\right) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">−</span><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap">和 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f\left(x_{k}\right)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap"> 可唯一确定一 个二次多项式, 若将它看成原函数 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>y</mi>
                                        <mo>=</mo>
                                        <mi>f</mi>
                                        <mo stretchy="false">(</mo>
                                        <mi>x</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">y=f(x)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span
                                    class="mopen">(</span><span class="mord mathnormal">x</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap"> 的近似,
                    则求解这个一元二次方程得到的根就可作为 迭代过程的下一个解。</span></div>
        </div>
        <div id="w8dSZhJooaCjTWhHd7pH3S" class="wolai-block wolai-text">
            <div><span class="inline-wrap">由于平面上通过 3 个点的曲线为抛物线, 由此导出的方法称为拋物线法。 抛物线法又分两种: 一种方法是根据 3 个已知点构造关于 x 的二次多项式
                    (抛物线), 求这个抛物线与 x 轴的交点作为下一个迭代解。求二次多项式的方法一般用揷值法, 因此 这种方法称为二次掐值法。关于揷值法的细节将在第 6 章介绍，这里不做讨论。</span></div>
        </div>
        <div id="dmEdHBw4DYoDRQ5jE4Yys1" class="wolai-block wolai-text">
            <div><span class="inline-wrap">二次揷值法得到的抛物线可能不与 x 轴相交, 因为二次方程末必有实数根。所以, 拹 物线法的另一种方法是将这 3 个点揷值为关于 y 的二次函数
                </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>P</mi>
                                            <mn>2</mn>
                                        </msub>
                                        <mo stretchy="false">(</mo>
                                        <mi>y</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">P_{2}(y)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.13889em;">P</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal"
                                    style="margin-right:0.03588em;">y</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">,
                    即得到通过这 3 点的“侧向抛物线”。这个二次函数 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>P</mi>
                                            <mn>2</mn>
                                        </msub>
                                        <mo stretchy="false">(</mo>
                                        <mi>y</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">P_{2}(y) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.13889em;">P</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal"
                                    style="margin-right:0.03588em;">y</span><span
                                    class="mclose">)</span></span></span></span></span><span
                    class="inline-wrap">满足方程</span></div>
        </div>
        <div id="fymq3cCzCu3oJVmgYi79fa" class="wolai-block wolai-text"><span class="katex-display"><span
                    class="katex"><span class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML"
                            display="block">
                            <semantics>
                                <mrow>
                                    <mo fence="true">{</mo>
                                    <mtable rowspacing="0.16em" columnalign="left" columnspacing="1em">
                                        <mtr>
                                            <mtd>
                                                <mstyle scriptlevel="0" displaystyle="false">
                                                    <mrow>
                                                        <msub>
                                                            <mi>x</mi>
                                                            <mrow>
                                                                <mi>k</mi>
                                                                <mo>−</mo>
                                                                <mn>2</mn>
                                                            </mrow>
                                                        </msub>
                                                        <mo>=</mo>
                                                        <msub>
                                                            <mi>P</mi>
                                                            <mn>2</mn>
                                                        </msub>
                                                        <mrow>
                                                            <mo fence="true">(</mo>
                                                            <mi>f</mi>
                                                            <mrow>
                                                                <mo fence="true">(</mo>
                                                                <msub>
                                                                    <mi>x</mi>
                                                                    <mrow>
                                                                        <mi>k</mi>
                                                                        <mo>−</mo>
                                                                        <mn>2</mn>
                                                                    </mrow>
                                                                </msub>
                                                                <mo fence="true">)</mo>
                                                            </mrow>
                                                            <mo fence="true">)</mo>
                                                        </mrow>
                                                    </mrow>
                                                </mstyle>
                                            </mtd>
                                        </mtr>
                                        <mtr>
                                            <mtd>
                                                <mstyle scriptlevel="0" displaystyle="false">
                                                    <mrow>
                                                        <msub>
                                                            <mi>x</mi>
                                                            <mrow>
                                                                <mi>k</mi>
                                                                <mo>−</mo>
                                                                <mn>1</mn>
                                                            </mrow>
                                                        </msub>
                                                        <mo>=</mo>
                                                        <msub>
                                                            <mi>P</mi>
                                                            <mn>2</mn>
                                                        </msub>
                                                        <mrow>
                                                            <mo fence="true">(</mo>
                                                            <mi>f</mi>
                                                            <mrow>
                                                                <mo fence="true">(</mo>
                                                                <msub>
                                                                    <mi>x</mi>
                                                                    <mrow>
                                                                        <mi>k</mi>
                                                                        <mo>−</mo>
                                                                        <mn>1</mn>
                                                                    </mrow>
                                                                </msub>
                                                                <mo fence="true">)</mo>
                                                            </mrow>
                                                            <mo fence="true">)</mo>
                                                        </mrow>
                                                    </mrow>
                                                </mstyle>
                                            </mtd>
                                        </mtr>
                                        <mtr>
                                            <mtd>
                                                <mstyle scriptlevel="0" displaystyle="false">
                                                    <mrow>
                                                        <msub>
                                                            <mi>x</mi>
                                                            <mi>k</mi>
                                                        </msub>
                                                        <mo>=</mo>
                                                        <msub>
                                                            <mi>P</mi>
                                                            <mn>2</mn>
                                                        </msub>
                                                        <mrow>
                                                            <mo fence="true">(</mo>
                                                            <mi>f</mi>
                                                            <mrow>
                                                                <mo fence="true">(</mo>
                                                                <msub>
                                                                    <mi>x</mi>
                                                                    <mi>k</mi>
                                                                </msub>
                                                                <mo fence="true">)</mo>
                                                            </mrow>
                                                            <mo fence="true">)</mo>
                                                        </mrow>
                                                    </mrow>
                                                </mstyle>
                                            </mtd>
                                        </mtr>
                                    </mtable>
                                </mrow>
                                <annotation encoding="application/x-tex">
                                    \left\{\begin{array}{l}x_{k-2}=P_{2}\left(f\left(x_{k-2}\right)\right)
                                    \\x_{k-1}=P_{2}\left(f\left(x_{k-1}\right)\right)
                                    \\x_{k}=P_{2}\left(f\left(x_{k}\right)\right)\\\end{array}\right.</annotation>
                            </semantics>
                        </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span class="strut"
                                style="height:3.6em;vertical-align:-1.55em;"></span><span class="minner"><span
                                    class="mopen"><span class="delimsizing mult"><span class="vlist-t vlist-t2"><span
                                                class="vlist-r"><span class="vlist" style="height:2.05em;"><span
                                                        style="top:-2.5em;"><span class="pstrut"
                                                            style="height:3.15em;"></span><span
                                                            class="delimsizinginner delim-size4"><span>⎩</span></span></span><span
                                                        style="top:-2.492em;"><span class="pstrut"
                                                            style="height:3.15em;"></span><span
                                                            style="height:0.016em;width:0.8889em;"><svg
                                                                xmlns="http://www.w3.org/2000/svg" width='0.8889em'
                                                                height='0.016em' style='width:0.8889em'
                                                                viewBox='0 0 888.89 16' preserveAspectRatio='xMinYMin'>
                                                                <path d='M384 0 H504 V16 H384z M384 0 H504 V16 H384z' />
                                                            </svg></span></span><span style="top:-3.15em;"><span
                                                            class="pstrut" style="height:3.15em;"></span><span
                                                            class="delimsizinginner delim-size4"><span>⎨</span></span></span><span
                                                        style="top:-4.292em;"><span class="pstrut"
                                                            style="height:3.15em;"></span><span
                                                            style="height:0.016em;width:0.8889em;"><svg
                                                                xmlns="http://www.w3.org/2000/svg" width='0.8889em'
                                                                height='0.016em' style='width:0.8889em'
                                                                viewBox='0 0 888.89 16' preserveAspectRatio='xMinYMin'>
                                                                <path d='M384 0 H504 V16 H384z M384 0 H504 V16 H384z' />
                                                            </svg></span></span><span style="top:-4.3em;"><span
                                                            class="pstrut" style="height:3.15em;"></span><span
                                                            class="delimsizinginner delim-size4"><span>⎧</span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:1.55em;"><span></span></span></span></span></span></span><span
                                    class="mord"><span class="mtable"><span class="arraycolsep"
                                            style="width:0.5em;"></span><span class="col-align-l"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:2.05em;"><span style="top:-4.21em;"><span
                                                                class="pstrut" style="height:3em;"></span><span
                                                                class="mord"><span class="mord"><span
                                                                        class="mord mathnormal">x</span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.3361em;"><span
                                                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mathnormal mtight"
                                                                                                    style="margin-right:0.03148em;">k</span><span
                                                                                                    class="mbin mtight">−</span><span
                                                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                    class="mspace"
                                                                    style="margin-right:0.2778em;"></span><span
                                                                    class="mrel">=</span><span class="mspace"
                                                                    style="margin-right:0.2778em;"></span><span
                                                                    class="mord"><span class="mord mathnormal"
                                                                        style="margin-right:0.13889em;">P</span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.3011em;"><span
                                                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                    class="mspace"
                                                                    style="margin-right:0.1667em;"></span><span
                                                                    class="minner"><span class="mopen delimcenter"
                                                                        style="top:0em;">(</span><span
                                                                        class="mord mathnormal"
                                                                        style="margin-right:0.10764em;">f</span><span
                                                                        class="mspace"
                                                                        style="margin-right:0.1667em;"></span><span
                                                                        class="minner"><span class="mopen delimcenter"
                                                                            style="top:0em;">(</span><span
                                                                            class="mord"><span
                                                                                class="mord mathnormal">x</span><span
                                                                                class="msupsub"><span
                                                                                    class="vlist-t vlist-t2"><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.3361em;"><span
                                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                                    class="pstrut"
                                                                                                    style="height:2.7em;"></span><span
                                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                                        class="mord mtight"><span
                                                                                                            class="mord mathnormal mtight"
                                                                                                            style="margin-right:0.03148em;">k</span><span
                                                                                                            class="mbin mtight">−</span><span
                                                                                                            class="mord mtight">2</span></span></span></span></span><span
                                                                                            class="vlist-s">​</span></span><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                            class="mclose delimcenter"
                                                                            style="top:0em;">)</span></span><span
                                                                        class="mclose delimcenter"
                                                                        style="top:0em;">)</span></span></span></span><span
                                                            style="top:-3.01em;"><span class="pstrut"
                                                                style="height:3em;"></span><span class="mord"><span
                                                                    class="mord"><span
                                                                        class="mord mathnormal">x</span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.3361em;"><span
                                                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mathnormal mtight"
                                                                                                    style="margin-right:0.03148em;">k</span><span
                                                                                                    class="mbin mtight">−</span><span
                                                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                    class="mspace"
                                                                    style="margin-right:0.2778em;"></span><span
                                                                    class="mrel">=</span><span class="mspace"
                                                                    style="margin-right:0.2778em;"></span><span
                                                                    class="mord"><span class="mord mathnormal"
                                                                        style="margin-right:0.13889em;">P</span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.3011em;"><span
                                                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                    class="mspace"
                                                                    style="margin-right:0.1667em;"></span><span
                                                                    class="minner"><span class="mopen delimcenter"
                                                                        style="top:0em;">(</span><span
                                                                        class="mord mathnormal"
                                                                        style="margin-right:0.10764em;">f</span><span
                                                                        class="mspace"
                                                                        style="margin-right:0.1667em;"></span><span
                                                                        class="minner"><span class="mopen delimcenter"
                                                                            style="top:0em;">(</span><span
                                                                            class="mord"><span
                                                                                class="mord mathnormal">x</span><span
                                                                                class="msupsub"><span
                                                                                    class="vlist-t vlist-t2"><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.3361em;"><span
                                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                                    class="pstrut"
                                                                                                    style="height:2.7em;"></span><span
                                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                                        class="mord mtight"><span
                                                                                                            class="mord mathnormal mtight"
                                                                                                            style="margin-right:0.03148em;">k</span><span
                                                                                                            class="mbin mtight">−</span><span
                                                                                                            class="mord mtight">1</span></span></span></span></span><span
                                                                                            class="vlist-s">​</span></span><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                                                            class="mclose delimcenter"
                                                                            style="top:0em;">)</span></span><span
                                                                        class="mclose delimcenter"
                                                                        style="top:0em;">)</span></span></span></span><span
                                                            style="top:-1.81em;"><span class="pstrut"
                                                                style="height:3em;"></span><span class="mord"><span
                                                                    class="mord"><span
                                                                        class="mord mathnormal">x</span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.3361em;"><span
                                                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mathnormal mtight"
                                                                                                    style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                    class="mspace"
                                                                    style="margin-right:0.2778em;"></span><span
                                                                    class="mrel">=</span><span class="mspace"
                                                                    style="margin-right:0.2778em;"></span><span
                                                                    class="mord"><span class="mord mathnormal"
                                                                        style="margin-right:0.13889em;">P</span><span
                                                                        class="msupsub"><span
                                                                            class="vlist-t vlist-t2"><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.3011em;"><span
                                                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                                                            class="pstrut"
                                                                                            style="height:2.7em;"></span><span
                                                                                            class="sizing reset-size6 size3 mtight"><span
                                                                                                class="mord mtight"><span
                                                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                                                    class="vlist-s">​</span></span><span
                                                                                class="vlist-r"><span class="vlist"
                                                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                    class="mspace"
                                                                    style="margin-right:0.1667em;"></span><span
                                                                    class="minner"><span class="mopen delimcenter"
                                                                        style="top:0em;">(</span><span
                                                                        class="mord mathnormal"
                                                                        style="margin-right:0.10764em;">f</span><span
                                                                        class="mspace"
                                                                        style="margin-right:0.1667em;"></span><span
                                                                        class="minner"><span class="mopen delimcenter"
                                                                            style="top:0em;">(</span><span
                                                                            class="mord"><span
                                                                                class="mord mathnormal">x</span><span
                                                                                class="msupsub"><span
                                                                                    class="vlist-t vlist-t2"><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.3361em;"><span
                                                                                                style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                                                    class="pstrut"
                                                                                                    style="height:2.7em;"></span><span
                                                                                                    class="sizing reset-size6 size3 mtight"><span
                                                                                                        class="mord mtight"><span
                                                                                                            class="mord mathnormal mtight"
                                                                                                            style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                                                            class="vlist-s">​</span></span><span
                                                                                        class="vlist-r"><span
                                                                                            class="vlist"
                                                                                            style="height:0.15em;"><span></span></span></span></span></span></span><span
                                                                            class="mclose delimcenter"
                                                                            style="top:0em;">)</span></span><span
                                                                        class="mclose delimcenter"
                                                                        style="top:0em;">)</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:1.55em;"><span></span></span></span></span></span><span
                                            class="arraycolsep" style="width:0.5em;"></span></span></span><span
                                    class="mclose nulldelimiter"></span></span></span></span></span></span></div>
        <div id="j277CUaAKd8zw7HEJqLdwt" class="wolai-block wolai-text">
            <div><span class="inline-wrap">只要 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>−</mo>
                                                    <mn>2</mn>
                                                </mrow>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f\left(x_{k-2}\right)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">−</span><span
                                                                        class="mord mtight">2</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap"> 、 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mrow>
                                                    <mi>k</mi>
                                                    <mo>−</mo>
                                                    <mn>1</mn>
                                                </mrow>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f\left(x_{k-1}\right) </annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span><span
                                                                        class="mbin mtight">−</span><span
                                                                        class="mord mtight">1</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap">和 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>f</mi>
                                        <mrow>
                                            <mo fence="true">(</mo>
                                            <msub>
                                                <mi>x</mi>
                                                <mi>k</mi>
                                            </msub>
                                            <mo fence="true">)</mo>
                                        </mrow>
                                    </mrow>
                                    <annotation encoding="application/x-tex">f\left(x_{k}\right)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.10764em;">f</span><span class="mspace"
                                    style="margin-right:0.1667em;"></span><span class="minner"><span
                                        class="mopen delimcenter" style="top:0em;">(</span><span class="mord"><span
                                            class="mord mathnormal">x</span><span class="msupsub"><span
                                                class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                        style="height:0.3361em;"><span
                                                            style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                                class="pstrut" style="height:2.7em;"></span><span
                                                                class="sizing reset-size6 size3 mtight"><span
                                                                    class="mord mtight"><span
                                                                        class="mord mathnormal mtight"
                                                                        style="margin-right:0.03148em;">k</span></span></span></span></span><span
                                                        class="vlist-s">​</span></span><span class="vlist-r"><span
                                                        class="vlist"
                                                        style="height:0.15em;"><span></span></span></span></span></span></span><span
                                        class="mclose delimcenter"
                                        style="top:0em;">)</span></span></span></span></span></span><span
                    class="inline-wrap"> 这 3 个值互不相等,抛物线 </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                        <mo>=</mo>
                                        <msub>
                                            <mi>P</mi>
                                            <mn>2</mn>
                                        </msub>
                                        <mo stretchy="false">(</mo>
                                        <mi>y</mi>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x=P_{2}(y)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.4306em;"></span><span
                                    class="mord mathnormal">x</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:1em;vertical-align:-0.25em;"></span><span
                                    class="mord"><span class="mord mathnormal"
                                        style="margin-right:0.13889em;">P</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord mathnormal"
                                    style="margin-right:0.03588em;">y</span><span
                                    class="mclose">)</span></span></span></span></span><span class="inline-wrap">
                    就可以构造出来, 并且它一定与 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>x</mi>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.4306em;"></span><span
                                    class="mord mathnormal">x</span></span></span></span></span><span
                    class="inline-wrap"> 轴有交点 (见图 2-10)。在交点处, </span><span><span class="katex"><span
                            class="katex-mathml"><math xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <mi>y</mi>
                                        <mo>=</mo>
                                        <mn>0</mn>
                                    </mrow>
                                    <annotation encoding="application/x-tex">y=0</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.625em;vertical-align:-0.1944em;"></span><span
                                    class="mord mathnormal" style="margin-right:0.03588em;">y</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span><span class="mrel">=</span><span
                                    class="mspace" style="margin-right:0.2778em;"></span></span><span class="base"><span
                                    class="strut" style="height:0.6444em;"></span><span
                                    class="mord">0</span></span></span></span></span><span class="inline-wrap">, 对应的 x
                    值为下一步迭代解 </span><span><span class="katex"><span class="katex-mathml"><math
                                xmlns="http://www.w3.org/1998/Math/MathML">
                                <semantics>
                                    <mrow>
                                        <msub>
                                            <mi>x</mi>
                                            <mrow>
                                                <mi>k</mi>
                                                <mo>+</mo>
                                                <mn>1</mn>
                                            </mrow>
                                        </msub>
                                        <mo>=</mo>
                                        <msub>
                                            <mi>P</mi>
                                            <mn>2</mn>
                                        </msub>
                                        <mo stretchy="false">(</mo>
                                        <mn>0</mn>
                                        <mo stretchy="false">)</mo>
                                    </mrow>
                                    <annotation encoding="application/x-tex">x_{k+1}=P_{2}(0)</annotation>
                                </semantics>
                            </math></span><span class="katex-html" aria-hidden="true"><span class="base"><span
                                    class="strut" style="height:0.6389em;vertical-align:-0.2083em;"></span><span
                                    class="mord"><span class="mord mathnormal">x</span><span class="msupsub"><span
                                            class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist"
                                                    style="height:0.3361em;"><span
                                                        style="top:-2.55em;margin-left:0em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span class="mord mathnormal mtight"
                                                                    style="margin-right:0.03148em;">k</span><span
                                                                    class="mbin mtight">+</span><span
                                                                    class="mord mtight">1</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.2083em;"><span></span></span></span></span></span></span><span
                                    class="mspace" style="margin-right:0.2778em;"></span><span
                                    class="mrel">=</span><span class="mspace"
                                    style="margin-right:0.2778em;"></span></span><span class="base"><span class="strut"
                                    style="height:1em;vertical-align:-0.25em;"></span><span class="mord"><span
                                        class="mord mathnormal" style="margin-right:0.13889em;">P</span><span
                                        class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span
                                                    class="vlist" style="height:0.3011em;"><span
                                                        style="top:-2.55em;margin-left:-0.1389em;margin-right:0.05em;"><span
                                                            class="pstrut" style="height:2.7em;"></span><span
                                                            class="sizing reset-size6 size3 mtight"><span
                                                                class="mord mtight"><span
                                                                    class="mord mtight">2</span></span></span></span></span><span
                                                    class="vlist-s">​</span></span><span class="vlist-r"><span
                                                    class="vlist"
                                                    style="height:0.15em;"><span></span></span></span></span></span></span><span
                                    class="mopen">(</span><span class="mord">0</span><span
                                    class="mclose">)</span></span></span></span></span><span
                    class="inline-wrap">这种方法称为逆二次插值法 (inverse quadratic interpolation)。</span></div>
        </div>
        <div id="qJRSgyqnJZJG8uJH1Bpjw1" class="wolai-block wolai-text">
            <div><span class="inline-wrap">理论上可以证明,两种抛物线法都具有超线性收敛速度，其共同的收敛阶是<span
                        class="jill"></span>1.839。此外，抛物线方法也是局部收敛的，因此迭代的初始值必须尽量接近准确解。</span></div>
        </div>
        <div id="hq25pGbXbbMbpQGcwp6NPz" class="wolai-block wolai-text">
            <div><span class="inline-wrap"></span><br /></div>
        </div>
        <div id="wr9FXcJsxsw13km9hr43Vk" class="wolai-block wolai-text">
            <div><span class="inline-wrap"></span><br /></div>
        </div>
        <div id="gsYhS3ZZU86Mw1Q5mKRizW" class="wolai-block">
            <figure class="wolai-center" style="width: 100%"><img src="media/image_8.png" style="width: 100%" />
            </figure>
        </div>
    </article>
    <footer></footer>
</body>

</html>
