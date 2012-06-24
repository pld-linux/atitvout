Summary:	Linux ATI TV Out support program	
Summary(pl):	Program do obs�ugi wyj�cia TV-out w kartach ATI
Name:		atitvout
Version:	0.4
Release:	0.1
License:	GPL 
Group:		Applications/Console
Source0:	http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/%{name}-%{version}.tar.gz
# Source0-md5:	f2915a435844aadcd4d8f9f62411283b
URL:		http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows to configure TV-out parameters in graphic cards
based on ATI's chips.

%description -l pl
Program pozwalaj�cy ustawia� r�ne parametry wyj�cia TV-out w kartach
graficznych na uk�adach ATI.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install atitvout $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HARDWARE README
%attr(755,root,root) %{_bindir}/atitvout
