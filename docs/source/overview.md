# Overview of Gmsh
## 1.1 Geometry module
## 1.2 Mesh module
Gmsh is a three-dimensional finite element mesh generator with a
build-in CAD engine and post-processor. Its design goal is to provide a
fast, light and user-friendly meshing tool with parametric input and
flexible visualization capabilities.
 Gmsh is built around four modules (geometry, mesh, solver and
post-processing), which can be controlled with the graphical user
interface (GUI; see <a href="https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-graphical-user-interface">Gmsh graphical user interface</a>), from the
command line (see <a href="https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-command_002dline-interface">Gmsh command-line interface</a>), using text files
written in Gmsh’s own scripting language (<samp>.geo</samp> files; see
<a href="https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-scripting-language">Gmsh scripting language</a>), or through the C++, C, Python, Julia and
Fortran application programming interface (API; see <a href="https://gmsh.info/doc/texinfo/gmsh.html#Gmsh-application-programming-interface">Gmsh application programming interface</a>).
</p>
<p>A brief description of the four modules is given hereafter, before an
overview of what Gmsh does best (... and what it is not so good at), and
some practical information on how to install and run Gmsh on your
computer.
</p>
<table class="menu" border="0" cellspacing="0">
<tbody><tr><td align="left" valign="top">• <a href="https://gmsh.info/doc/texinfo/gmsh.html#Geometry-module" accesskey="1">Geometry module</a></td><td>&nbsp;&nbsp;</td><td align="left" valign="top">
</td></tr>
<tr><td align="left" valign="top">• <a href="https://gmsh.info/doc/texinfo/gmsh.html#Mesh-module" accesskey="2">Mesh module</a></td><td>&nbsp;&nbsp;</td><td align="left" valign="top">
</td></tr>
<tr><td align="left" valign="top">• <a href="https://gmsh.info/doc/texinfo/gmsh.html#Solver-module" accesskey="3">Solver module</a></td><td>&nbsp;&nbsp;</td><td align="left" valign="top">
</td></tr>
<tr><td align="left" valign="top">• <a href="https://gmsh.info/doc/texinfo/gmsh.html#Post_002dprocessing-module" accesskey="4">Post-processing module</a></td><td>&nbsp;&nbsp;</td><td align="left" valign="top">
</td></tr>
<tr><td align="left" valign="top">• <a href="https://gmsh.info/doc/texinfo/gmsh.html#What-Gmsh-is-pretty-good-at" accesskey="5">What Gmsh is pretty good at</a></td><td>&nbsp;&nbsp;</td><td align="left" valign="top">
</td></tr>
<tr><td align="left" valign="top">• <a href="https://gmsh.info/doc/texinfo/gmsh.html#and-what-Gmsh-is-not-so-good-at" accesskey="6">and what Gmsh is not so good at</a></td><td>&nbsp;&nbsp;</td><td align="left" valign="top">
</td></tr>
<tr><td align="left" valign="top">• <a href="https://gmsh.info/doc/texinfo/gmsh.html#Installing-and-running-Gmsh-on-your-computer" accesskey="7">Installing and running Gmsh on your computer</a></td><td>&nbsp;&nbsp;</td><td align="left" valign="top">
</td></tr>
</tbody></table>


<hr>
<span id="Geometry-module"></span><div class="header">
<p>
Next: <a href="https://gmsh.info/doc/texinfo/gmsh.html#Mesh-module" accesskey="n" rel="next">Mesh module</a>, Previous: <a href="https://gmsh.info/doc/texinfo/gmsh.html#Overview-of-Gmsh" accesskey="p" rel="prev">Overview of Gmsh</a>, Up: <a href="https://gmsh.info/doc/texinfo/gmsh.html#Overview-of-Gmsh" accesskey="u" rel="up">Overview of Gmsh</a> &nbsp; [<a href="https://gmsh.info/doc/texinfo/gmsh.html#SEC_Contents" title="Table of contents" rel="contents">Contents</a>][<a href="https://gmsh.info/doc/texinfo/gmsh.html#Concept-index" title="Index" rel="index">Index</a>]</p>
</div>
<span id="Geometry-module-1"></span><h3 class="section">1.1 Geometry module</h3>

