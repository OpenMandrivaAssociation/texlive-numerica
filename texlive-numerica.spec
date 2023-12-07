Name:		texlive-numerica
Version:	68021
Release:	1
Summary:	Numerically evaluate mathematical expressions in LaTeX form
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/numerica
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/numerica.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines a command to wrap around a mathematical
expression in its LaTeX form and, once values are assigned to
variables, numerically evaluate it. The intent is to avoid the
need to modify the LaTeX form of the expression being
evaluated. For programs with a preview facility like LyX, or
compile-as-you-go systems, interactive back-of-envelope
calculations and numerical exploration are possible within the
document being worked on. The package requires the bundles
l3kernel and l3packages, and the amsmath and mathtools
packages.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/numerica
%doc %{_texmfdistdir}/doc/latex/numerica

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
