Summary:	Thai Input Method Engine for SCIM
Summary(pl.UTF-8):	Silnik wprowadzania znaków tajskich dla SCIM
Name:		scim-thai
Version:	0.1.2
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.gz
# Source0-md5:	ac33b24f949245f7c9971a21e7a4e570
URL:		http://linux.thai.net/projects/scim-thai
BuildRequires:	libstdc++-devel
BuildRequires:	libthai-devel
BuildRequires:	scim-devel >= 0.99.8
Requires:	scim >= 0.99.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM-Thai is a SCIM IMEngine module for Thai, based on the libthai
library.

Currently, it supports Ketmanee, TIS-820.2538, and Pattachote keyboard
layouts and can validate input sequences at 3 levels of strictness.

For applications that support surrounding text retrieval/deleting, it
also corrects invalid input sequences.

%description -l pl.UTF-8
SCIM-Thai to moduł IMEngine dla SCIM, pozwalający na wprowadzanie
znaków tajskich, oparty na bibliotece libthai.

Obecnie obsługuje układy klawiatury Ketmanee, TIS-820.2538 oraz
Pattachote i jest w stanie sprawdzać poprawność sekwencji wejściowych
na trzech poziomach dokładności.

W aplikacjach obsługujących pobieranie i usuwanie sąsiadującego tekstu
potrafi także poprawiać błędne sekwencje wejściowe.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/thai.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/thai-imengine-setup.so
%{_datadir}/scim/icons/scim-thai.png
