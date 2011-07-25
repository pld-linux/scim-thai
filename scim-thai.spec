Summary:	Thai Input Method Engine for SCIM
Name:		scim-thai
Version:	0.1.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	ftp://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.gz
# Source0-md5:	caa84f54fedf4fe1bcf50dfe69ec112d
URL:		http://linux.thai.net/projects/scim-thai
BuildRequires:	scim-devel
BuildRequires:	libthai-devel
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SCIM-Thai is a SCIM IMEngine module for Thai, based on the libthai
library.

Currently, it supports Ketmanee, TIS-820.2538, and Pattachote keybaord
layouts and can validate input sequences at 3 levels of strictness.

For applications that support surrounding text retrieval/deleting, it
also corrects invalid input sequences.

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
%doc AUTHORS COPYING README ChangeLog
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/thai.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/thai-imengine-setup.so
%{_datadir}/scim/icons/scim-thai.png
