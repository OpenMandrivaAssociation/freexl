%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	Library to extract valid data from within an Excel spreadsheet
Name:		freexl
Version:	1.0.0g
Release:	2
License:	MPL or GPLv2+ or LGPLv2.1+
Group:		System/Libraries
Url:		https://www.gaia-gis.it/fossil/freexl/index
Source0:	http://www.gaia-gis.it/gaia-sins/%{name}-%{version}.tar.gz

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
%setup -q

%build
autoreconf
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

