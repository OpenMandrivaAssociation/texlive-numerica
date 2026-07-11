%global tl_name numerica
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0.0
Release:	%{tl_revision}.1
Summary:	Numerically evaluate mathematical expressions in LaTeX form
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/numerica
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines a command to wrap around a mathematical expression
in its LaTeX form and, once values are assigned to variables,
numerically evaluate it. The intent is to avoid the need to modify the
LaTeX form of the expression being evaluated. For programs with a
preview facility like LyX, or compile-as-you-go systems, interactive
back-of-envelope calculations and numerical exploration are possible
within the document being worked on. The package requires the bundles
l3kernel and l3packages, and the amsmath and mathtools packages.

