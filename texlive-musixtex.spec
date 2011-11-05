# revision 23303
# category Package
# catalog-ctan /macros/musixtex
# catalog-date 2011-07-18 20:08:03 +0200
# catalog-license gpl
# catalog-version 1.15 (2011-07-18)
Name:		texlive-musixtex
Version:	1.15 (2011-07-18)
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
MusiXTeX is a set of macros, based on the earlier MusicTeX, for
typesetting music with TeX. MusicTeX demonstrated that TeX
alone cannot practically typeset good-looking ties and slurs.
There is therefore a separate processor, musixflx, in the
bundle, which uses the output of MusiXTeX to position the
slurs. As a result, MusixTeX is a three-pass system: TeX,
musixflx, and TeX again. This version of MusixTeX builds upon
work by Andreas Egler, whose own version is no longer being
developed. Raw MusiXTeX macros are universally acknowledged to
be tricky to write: most users employ the pmx preprocessor,
which takes much of the strain.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/musixflx
%{_bindir}/musixtex
%{_texmfdistdir}/dvips/musixtex/psslurs.pro
%{_texmfdistdir}/fonts/map/dvips/musixtex/musix.map
%{_texmfdistdir}/fonts/source/public/musixtex/musexgen.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musix11.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musix13.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musix16.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musix20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musix24.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musix25.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musix29.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musixgen.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musixsps.mf
%{_texmfdistdir}/fonts/source/public/musixtex/musixspx.mf
%{_texmfdistdir}/fonts/source/public/musixtex/mxsk.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xdrawsl.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xdrawzl.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreg11.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreg13.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreg16.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreg20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreg24.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreg25.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreg29.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xgreggen.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld11.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld13.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld16.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld24.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld29.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsld29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsldd20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xsldu20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslgen.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslgend.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslgenu.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd11.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd13.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd16.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd24.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd29.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhd29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu11.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu13.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu16.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu24.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu29.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhu29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhz-o.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhz.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhz20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslhz20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu11.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu11d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu13.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu13d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu16.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu16d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu24.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu24d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu29.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslu29d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslud20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslup20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslz.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslz20.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xslz20d.mf
%{_texmfdistdir}/fonts/source/public/musixtex/xtie20.mf
%{_texmfdistdir}/fonts/tfm/public/musixtex/musix11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musix13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musix16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musix20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musix24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musix25.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musix29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musixsps.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/musixspx.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/mxsk.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xgreg11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xgreg13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xgreg16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xgreg20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xgreg24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xgreg29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsld29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsldd20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xsldu20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhd29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu20m.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhu29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhz20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslhz20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu11.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu11d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu13.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu13d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu16.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu16d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu24.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu24d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu29.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslu29d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslud20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslup20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslz20.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xslz20d.tfm
%{_texmfdistdir}/fonts/tfm/public/musixtex/xtie20.tfm
%{_texmfdistdir}/fonts/type1/public/musixtex/musix11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/musix13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/musix16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/musix20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/musix24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/musix29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/musixsps.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/musixspx.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/mxsk.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xgreg11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xgreg13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xgreg16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xgreg20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xgreg24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xgreg29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsld29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsldd20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xsldu20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhd29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhu29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhz20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslhz20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu11.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu11d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu13.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu13d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu16.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu16d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu24.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu24d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu29.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslu29d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslud20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslup20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslz20.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xslz20d.pfb
%{_texmfdistdir}/fonts/type1/public/musixtex/xtie20.pfb
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
%doc %{_texmfdistdir}/doc/generic/musixtex/ChangeLog-115.txt
%doc %{_texmfdistdir}/doc/generic/musixtex/ChangeLog-T114.txt
%doc %{_texmfdistdir}/doc/generic/musixtex/ChangeLog-musixdoc-115.txt
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
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/coulhack.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottieng.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottieng.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottiger.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottiger.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottigra.pdf
%doc %{_texmfdistdir}/doc/generic/musixtex/notationMistakes/sottigra.tex
%doc %{_texmfdistdir}/doc/generic/musixtex/psfonts/CHANGES.psfonts
%doc %{_texmfdistdir}/doc/generic/musixtex/psfonts/README.psfonts
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
%doc %{_tlpkgobjdir}/*.tlpobj

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
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
