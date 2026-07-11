%global tl_name musixtex
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.41
Release:	%{tl_revision}.1
Summary:	Sophisticated music typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/musixtex
License:	gpl2+
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(musixtex.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
MusiXTeX provides a set of macros, based on the earlier MusicTeX, for
typesetting music with TeX. To produce optimal spacing, MusiXTeX is a
three-pass system: etex, musixflx, and etex again. (Musixflx is a lua
script that is provided in the bundle.) The three-pass process,
optionally followed by processing for printed output, is automated by
the musixtex wrapper script. The package uses its own specialised fonts,
which must be available on the system for musixtex to run. This version
of MusiXTeX builds upon work by Andreas Egler, whose own version is no
longer being developed. The MusiXTeX macros are universally acknowledged
to be challenging to use directly: the pmx preprocessor compiles a
simpler input language to MusiXTeX macros..

