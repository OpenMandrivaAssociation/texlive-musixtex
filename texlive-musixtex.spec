# revision 24518
# category Package
# catalog-ctan /macros/musixtex
# catalog-date 2011-10-24 18:06:47 +0200
# catalog-license gpl
# catalog-version 1.15 (2011-10-23)
Name:		texlive-musixtex
Version:	1.15
Release:	2
Summary:	Sophisticated music typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/musixtex
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/musixtex.source.tar.xz
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
%{_texmfdistdir}/dvips/musixtex/psslurs.pro
%{_texmfdistdir}/scripts/musixtex/Windows/musixflx.bat
%{_texmfdistdir}/scripts/musixtex/Windows/musixtex.bat
%{_texmfdistdir}/scripts/musixtex/musixflx.lua
%{_texmfdistdir}/scripts/musixtex/musixtex.lua
%{_texmfdistdir}/tex/generic/musixtex/musixadd.tex
%{_texmfdistdir}/tex/generic/musixtex/musixbar.tex
%{_texmfdistdir}/tex/generic/musixtex/musixbbm.tex
%{_texmfdistdir}/tex/generic/musixtex/musixblx.tex
%{_texmfdistdir}/tex/generic/musixtex/musixbm.tex
%{_texmfdistdir}/tex/generic/musixtex/musixcho.tex
%{_texmfdistdir}/tex/generic/musixtex/musixcpt.tex
%{_texmfdistdir}/tex/generic/musixtex/musixcrd.tex
%{_texmfdistdir}/tex/generic/musixtex/musixdat.tex
%{_texmfdistdir}/tex/generic/musixtex/musixdbr.tex
%{_texmfdistdir}/tex/generic/musixtex/musixdia.tex
%{_texmfdistdir}/tex/generic/musixtex/musixeng.tex
%{_texmfdistdir}/tex/generic/musixtex/musixesf.tex
%{_texmfdistdir}/tex/generic/musixtex/musixevo.tex
%{_texmfdistdir}/tex/generic/musixtex/musixext.tex
%{_texmfdistdir}/tex/generic/musixtex/musixfll.sty
%{_texmfdistdir}/tex/generic/musixtex/musixfll.tex
%{_texmfdistdir}/tex/generic/musixtex/musixgre.tex
%{_texmfdistdir}/tex/generic/musixtex/musixgui.tex
%{_texmfdistdir}/tex/generic/musixtex/musixhor.tex
%{_texmfdistdir}/tex/generic/musixtex/musixhou.tex
%{_texmfdistdir}/tex/generic/musixtex/musixinv.tex
%{_texmfdistdir}/tex/generic/musixtex/musixlit.tex
%{_texmfdistdir}/tex/generic/musixtex/musixlyr.tex
%{_texmfdistdir}/tex/generic/musixtex/musixmad.tex
%{_texmfdistdir}/tex/generic/musixtex/musixper.tex
%{_texmfdistdir}/tex/generic/musixtex/musixpoi.tex
%{_texmfdistdir}/tex/generic/musixtex/musixps.tex
%{_texmfdistdir}/tex/generic/musixtex/musixref.tex
%{_texmfdistdir}/tex/generic/musixtex/musixslu.tex
%{_texmfdistdir}/tex/generic/musixtex/musixsqr.tex
%{_texmfdistdir}/tex/generic/musixtex/musixste.tex
%{_texmfdistdir}/tex/generic/musixtex/musixstf.tex
%{_texmfdistdir}/tex/generic/musixtex/musixstr.tex
%{_texmfdistdir}/tex/generic/musixtex/musixsty.tex
%{_texmfdistdir}/tex/generic/musixtex/musixtex.tex
%{_texmfdistdir}/tex/generic/musixtex/musixtmr.tex
%{_texmfdistdir}/tex/generic/musixtex/musixtri.tex
%{_texmfdistdir}/tex/latex/musixtex/musixcpt.sty
%{_texmfdistdir}/tex/latex/musixtex/musixcrd.sty
%{_texmfdistdir}/tex/latex/musixtex/musixltx.tex
%{_texmfdistdir}/tex/latex/musixtex/musixtex.sty
%doc %{_texmfdistdir}/doc/generic/musixtex/ChangeLog
%doc %{_texmfdistdir}/doc/generic/musixtex/ChangeLog-115.txt
%doc %{_texmfdistdir}/doc/generic/musixtex/ChangeLog-T114.txt
%doc %{_texmfdistdir}/doc/generic/musixtex/ChangeLog-musixdoc-115.txt
%doc %{_texmfdistdir}/doc/generic/musixtex/README
%doc %{_texmfdistdir}/doc/generic/musixtex/addons/curly.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/addons/tuplet.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/addons/underbracket.sty
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/8bitchar.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/adagio.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/albinoni.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/angescam.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/angescao.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/angescax.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/avemaria.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/avemarid.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/avemaril.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/avemario.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/avemarix.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/avemaroo.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/aveverch.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/aveverdd.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/aveveruc.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/aveverud.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/aveverum.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/changecontext.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/chanson.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/coulhack.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/dissonan.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/fantaisc.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/fantaisd.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/fantaisi.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/fantcmol.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/fantfuga.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/fugcmoll.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/fugue.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/gloriab.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/glorias.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/gloriax.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/gymnoman.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/ilestne.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/ilestnex.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/ilfaitda.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/ilfaitdx.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/kv315.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/kv315f.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/kv315h.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/kv315o.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/kv315org.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/marcello.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/marcon1.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/marcon2.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/marcon3.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/marconf.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/marconh.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/marcono.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/musixdbrexample.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/onuitbri.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/onuitbrr.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/onuitbrx.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/ossiaexa.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/ostinato.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/pacifiqb.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/pacifiqn.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/pacifiqt.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/parnasum.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/partitur.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/prelfug.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/prelude.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/pslurvgap.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/quod.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/racine.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/recit.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/recueil.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/rests.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/reves.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/romances.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/scale.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/souvenir.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/souvenix.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/tierce.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/traeumer.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/widor.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/widor_16.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/examples/widor_20.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/gpl.txt
%doc %{_texmfdistdir}/doc/generic/musixtex/musixcrd/README.musixcrd
%doc %{_texmfdistdir}/doc/generic/musixtex/musixcrd/doc.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/musixdoc.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/musixdoc.sty
%doc %{_texmfdistdir}/doc/generic/musixtex/musixdoc.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/musixlyr/README.musixlyr
%doc %{_texmfdistdir}/doc/generic/musixtex/musixlyr/examples/nonmoriar.dvi
%doc %{_texmfdistdir}/doc/generic/musixtex/musixlyr/examples/nonmoriar.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/musixlyr/examples/nonmoriar.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/musixlyr/mxlyrdoc.dvi
%doc %{_texmfdistdir}/doc/generic/musixtex/musixlyr/mxlyrdoc.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/musixlyr/mxlyrdoc.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/musixtex-install.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/musixtex-install.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/coulhack.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottieng.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottieng.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottiger.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottiger.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottigra.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottigra.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/psslurs/README.psslurs
%doc %{_texmfdistdir}/doc/generic/musixtex/psslurs/slurs.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/psslurs/slurs.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/reference/musixre1.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/reference/musixre1.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/scripts/musixflx.1
%doc %{_texmfdistdir}/doc/generic/musixtex/scripts/musixflx.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/scripts/musixtex.1
%doc %{_texmfdistdir}/doc/generic/musixtex/scripts/musixtex.pdf
%doc %{_mandir}/man1/musixflx.1*
%doc %{_texmfdir}/doc/man/man1/musixflx.man1.pdf
%doc %{_mandir}/man1/musixtex.1*
%doc %{_texmfdir}/doc/man/man1/musixtex.man1.pdf
#- source
%doc %{_texmfdistdir}/source/generic/musixtex/musixcrd/doc.tex
%doc %{_texmfdistdir}/source/generic/musixtex/musixcrd/makefile
%doc %{_texmfdistdir}/source/generic/musixtex/musixcrd/musixcrd.dtx
%doc %{_texmfdistdir}/source/generic/musixtex/musixcrd/readme
%doc %{_texmfdistdir}/source/generic/musixtex/musixcrd/strip.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/musixtex/musixflx.lua musixflx
    ln -sf %{_texmfdistdir}/scripts/musixtex/musixtex.lua musixtex
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
