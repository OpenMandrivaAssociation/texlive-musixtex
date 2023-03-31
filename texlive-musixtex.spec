Name:		texlive-musixtex
Version:	60382
Release:	2
Summary:	Sophisticated music typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/musixtex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Provides:	texlive-musixtex.bin = %{EVRD}

%description
MusiXTeX provides a set of macros, based on the earlier
MusicTeX, for typesetting music with TeX. To produce optimal
spacing, MusixTeX is a three-pass system: etex, musixflx, and
etex again. (Musixflx is a lua script that is provided in the
bundle.) The three-pass process, optionally followed by
processing for printed output, is automated by the musixtex
wrapper script. The package uses its own specialised fonts,
which must be available on the system for musixtex to run. This
version of MusixTeX builds upon work by Andreas Egler, whose
own version is no longer being developed. The MusiXTeX macros
are universally acknowledged to be challenging to use directly:
the pmx preprocessor compiles a simpler input language to
MusixTeX macros..

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/musixflx
%{_bindir}/musixtex
%{_texmfdistdir}/dvips/musixtex
%{_texmfdistdir}/scripts/musixtex
%{_texmfdistdir}/tex/generic/musixtex
%{_texmfdistdir}/tex/latex/musixtex
%doc %{_texmfdistdir}/doc/generic/musixtex
%doc %{_mandir}/man1/musixflx.1*
%doc %{_texmfdistdir}/doc/man/man1/musixflx.man1.pdf
%doc %{_mandir}/man1/musixtex.1*
%doc %{_texmfdistdir}/doc/man/man1/musixtex.man1.pdf
#- source
%doc %{_texmfdistdir}/source/generic/musixtex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/musixtex/musixflx.lua musixflx
ln -sf %{_texmfdistdir}/scripts/musixtex/musixtex.lua musixtex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
