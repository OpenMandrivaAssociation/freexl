%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d
%define beta RC2

Summary:	Library to extract valid data from within an Excel spreadsheet
Name:		freexl
Version:	2.0.0
Release:	%{?beta:0.%{beta}.}2
License:	MPL or GPLv2+ or LGPLv2.1+
Group:		System/Libraries
Url:		https://www.gaia-gis.it/fossil/freexl/index
Source0:	http://www.gaia-gis.it/gaia-sins/freexl-sources/freexl-%{version}%{?beta:-%{beta}}.tar.gz
BuildRequires:	pkgconfig(minizip)
BuildRequires:	pkgconfig(expat)
BuildRequires:	make
BuildRequires:	autoconf
BuildRequires:	automake

%description
FreeXL is an open source library to extract valid data from within an Excel
(.xls) spreadsheet.

FreeXL design goals:

- to be simple and lightweight
- to be stable, robust and efficient
- to be easily and universally portable
- completely ignoring any GUI-related oddity

Note that the final goal means that FreeXL ignores at all fonts, sizes
and alignments, and most formats. It ignores Pivot Table, Charts, Formulas,
Visual Basic macros and so on. FreeXL is structurally simple and quite
light-weight.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Library to extract valid data from within an Excel spreadsheet

%description -n %{libname}
FreeXL is an open source library to extract valid data from within an Excel
(.xls) spreadsheet.

FreeXL design goals:

- to be simple and lightweight
- to be stable, robust and efficient
- to be easily and universally portable
- completely ignoring any GUI-related oddity

Note that the final goal means that FreeXL ignores at all fonts, sizes
and alignments, and most formats. It ignores Pivot Table, Charts, Formulas,
Visual Basic macros and so on. FreeXL is structurally simple and quite
light-weight.

%files -n %{libname}
%{_libdir}/libfreexl.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Library to extract valid data from within an Excel spreadsheet
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
FreeXL is an open source library to extract valid data from within an Excel
(.xls) spreadsheet.

This package contains development files.

%files -n %{devname}
%doc AUTHORS README
%{_libdir}/libfreexl.so
%{_libdir}//pkgconfig/freexl.pc
%{_includedir}/freexl.h

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{version}%{?beta:-%{beta}}
autoreconf
%configure

%build
%make_build

%install
%make_install
