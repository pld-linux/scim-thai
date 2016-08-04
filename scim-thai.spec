Summary:	Thai Input Method Engine for SCIM
Summary(pl.UTF-8):	Silnik wprowadzania znaków tajskich dla SCIM
Name:		scim-thai
Version:	0.1.4
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
# Source0-md5:	afe6dc49bb51a78158480591b14693a2
URL:		https://linux.thai.net/projects/scim-thai
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	gtk+3-devel >= 3.16
BuildRequires:	libstdc++-devel
BuildRequires:	libthai-devel
BuildRequires:	scim-devel >= 1.4.13
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk+3 >= 3.16
Requires:	scim >= 1.4.13
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
