Name:		texlive-quantikz
Version:	67206
Release:	1
Summary:	Draw quantum circuit diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/quantikz
License:	cc-by-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quantikz.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/quantikz.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The purpose of this package is to extend TikZ with the
functionality for drawing quantum circuit diagrams.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/quantikz
%doc %{_texmfdistdir}/doc/latex/quantikz

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
