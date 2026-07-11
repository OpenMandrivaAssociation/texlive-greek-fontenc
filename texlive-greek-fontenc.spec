%global tl_name greek-fontenc
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.6
Release:	%{tl_revision}.1
Summary:	LICR macros and encoding definition files for Greek
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/greek/greek-fontenc
License:	lppl1.3 bsd2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-fontenc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/greek-fontenc.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
LICR macros for characters from the Greek script and encoding definition
files for Greek text font encodings.

