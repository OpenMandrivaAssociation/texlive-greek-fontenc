# revision 32301
# category Package
# catalog-ctan /language/greek/greek-fontenc
# catalog-date 2013-12-02 17:59:53 +0100
# catalog-license lppl1.3
# catalog-version 0.11.1
Name:		texlive-greek-fontenc
Version:	0.11.1
Release:	5
Summary:	LICR macros and encoding definition files for Greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/greek-fontenc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-fontenc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-fontenc.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides Greek LICR macro definitions and encoding
definition files for Greek text font encodings for use with
fontenc.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/greek-fontenc/alphabeta-euenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/alphabeta.sty
%{_texmfdistdir}/tex/latex/greek-fontenc/greek-euenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/greek-fontenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/lgrenc.def
%{_texmfdistdir}/tex/latex/greek-fontenc/textalpha.sty
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/README
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/README.html
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-euenc.def.html
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-euenc.def.txt
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-test.pdf
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta-test.tex
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/alphabeta.sty.html
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/diacritics.pdf
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/diacritics.tex
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/euenc-test.pdf
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/euenc-test.tex
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/greek-euenc.def.html
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/greek-fontenc.def.html
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/greekhyperref.pdf
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/greekhyperref.tex
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/lgr2licr.lua
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/lgr2licr.lua.html
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/lgrenc-test.pdf
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/lgrenc-test.tex
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/lgrenc.def.html
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/textalpha-test.pdf
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/textalpha-test.tex
%doc %{_texmfdistdir}/doc/latex/greek-fontenc/textalpha.sty.html

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
