Summary:	Linux ATI TV-out support program	
Summary(pl):	Program do obs³ugi wyj¶cia TV-out w kartach ATI
Name:		atitvout
Version:	0.4
Release:	2
License:	GPL
Group:		Applications/Console
Source0:	http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/%{name}-%{version}.tar.gz
# Source0-md5:	f2915a435844aadcd4d8f9f62411283b
Source1:	%{name}-man
URL:		http://www.stud.uni-hamburg.de/users/lennart/projects/atitvout/
BuildRequires:	sed >= 4.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program allows to configure TV-out parameters in graphic cards
based on ATI's chips.

%description -l pl
Program pozwalaj±cy ustawiaæ ró¿ne parametry wyj¶cia TV-out w kartach
graficznych na uk³adach ATI.

%prep
%setup -q -n %{name}

%build
sed -i -e 's@-g -Wall@%{rpmcflags}@' lrmi-0.6/Makefile
sed -i -e 's@-Wall -O2 -g@%{rpmcflags}@' Makefile
%{__make} \
	CC="%{__cc}" 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man1}

install atitvout $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HARDWARE README
%attr(755,root,root) %{_sbindir}/atitvout
%{_mandir}/man1/*
