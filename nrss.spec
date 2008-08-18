Summary:	NCurses Feed Reader
Name:		nrss
Version:	0.3.9
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://ncurses-rss.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	0673d5b18cee1f7229bed45db05f3c3e
URL:		http://www.codezen.org/nrss/
BuildRequires:	ncurses-ext-devel
BuildRequires:	wget
Requires:	wget
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NCurses Feed Reader

%prep
%setup -q

%build
%{__make} \
	PREFIX=%{_prefix} \
	CC="%{__cc}" \
	DESTDIR=$RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
