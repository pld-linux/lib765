Summary:	765 FDC
Summary(pl):	Biblioteka 765
Name:		lib765
Version:	0.3.0
Release:	1
License:	LGPL
Group:		Development/Libraries
Source0:	http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdsk-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc Controller
[FDC] as used in Amstrad computers such as the PCW, CPC and Spectrum +3. At
present it is not a "full" 765; features not used in the PCW BIOS (such as:
DMA; multisector reads/writes; multitrack mode) are either left unimplemented
or incomplete.
  
"765" is released under the GNU Library GPL.
%description -l pl
"765" jest emulacj± kontrolera dysków elastycznych uPD765a (AKA Intel 8272)
u¿ywanego w komputerach Amstrada, takich jak PCW, CPC czy Spectrum +3.
Na razie nie jest to "pe³ne" 765; w³a¶ciwo¶ci nieu¿ywane w BIOSie PCW
(takie jak: DMA; odczyt/zapis wielu sektorów; tryb wielo¶cie¿kowy) s± albo
niezaimplementowane albo ich emulacja jest niepe³na.

"765" jest wypuszczone ma licencji LGPL.

%package devel
Summary:	765 library - development
Summary(pl):	Czê¶æ dla programistów biblioteki 765
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The lib765-devel package contains the header files and documentation
needed to develop applications with lib765.

%description devel -l pl
Pakiet lib765-devel zawiera pliki nag³ówkowe i dokumentacjê potrzebne
do kompilowania aplikacji korzystaj±cych z lib765.

%package static
Summary:	765 static library
Summary(pl):	Statyczna biblioteka lib765
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
The lib765-static package contains the static libraries of lib765.

%description static -l pl
Statyczna wersja biblioteki lib765.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib765.so.*

%files devel
%defattr(644,root,root,755)
%doc doc/765.txt 
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib765.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
