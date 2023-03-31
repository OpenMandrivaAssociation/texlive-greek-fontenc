Name:		texlive-greek-fontenc
Version:	63604
Release:	2
Summary:	LICR macros and encoding definition files for Greek
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/greek/greek-fontenc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-fontenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-fontenc.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/greek-fontenc
%doc %{_texmfdistdir}/doc/latex/greek-fontenc

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
