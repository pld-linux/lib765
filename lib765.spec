#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	765 FDC library
Summary(pl.UTF-8):	Biblioteka FDC 765
Name:		lib765
Version:	0.3.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://www.seasip.demon.co.uk/Unix/LibDsk/%{name}-%{version}.tar.gz
# Source0-md5:	fd916b3fe613c39e07540bdbc0effc7f
URL:		http://www.seasip.demon.co.uk/Unix/LibDsk/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libdsk-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"765" is an emulation of the uPD765a (AKA Intel 8272) Floppy Disc
Controller [FDC] as used in Amstrad computers such as the PCW, CPC and
Spectrum +3. At present it is not a "full" 765; features not used in
the PCW BIOS (such as: DMA; multisector reads/writes; multitrack mode)
are either left unimplemented or incomplete.

"765" is released under the GNU Library GPL.

%description -l pl.UTF-8
"765" jest emulacją kontrolera dysków elastycznych uPD765a (znanego
też jako Intel 8272) używanego w komputerach Amstrada, takich jak PCW,
CPC czy Spectrum +3. Na razie nie jest to "pełne" 765; właściwości
nieużywane w BIOS-ie PCW (takie jak: DMA; odczyt/zapis wielu sektorów;
tryb wielościeżkowy) są albo niezaimplementowane albo ich emulacja
jest niepełna.

"765" jest wypuszczone ma licencji LGPL.

%package devel
Summary:	765 library - development files
Summary(pl.UTF-8):	Pliki programistyczne biblioteki 765
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libdsk-devel

%description devel
The lib765-devel package contains the header files and documentation
needed to develop applications with lib765.

%description devel -l pl.UTF-8
Pakiet lib765-devel zawiera pliki nagłówkowe i dokumentację potrzebne
do kompilowania aplikacji korzystających z lib765.

%package static
Summary:	765 static library
Summary(pl.UTF-8):	Statyczna biblioteka lib765
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
This package contains the static lib765 library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki lib765.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib765.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/765.txt
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib765.la
%{_includedir}/*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
