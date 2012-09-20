%define major		1
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Name:		freexl
Summary:	Library to extract valid data from within an Excel spreadsheet
Version:	1.0.0d
Release:	1
License:	MPL or GPLv2 or LGPLv2.1
Group:		System/Libraries
URL:		https://www.gaia-gis.it/fossil/freexl/index
Source0:	http://www.gaia-gis.it/gaia-sins/freexl-1.0.0d.tar.gz
Patch0:		freexl-1.0.0d-mdv-linking.patch

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

%package -n %{develname}
Summary:	Library to extract valid data from within an Excel spreadsheet
Group:		Development/C

%description -n %{libname}
FreeXL is an open source library to extract valid data from within an Excel
(.xls) spreadsheet.

This package contains development files.

%prep
%setup -q
%patch0 -p1
autoreconf

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libfreexl.so.%{major}*

%files -n %{develname}
%doc AUTHORS README
%{_libdir}/libfreexl.so
%{_libdir}//pkgconfig/freexl.pc
%{_includedir}/freexl.h
