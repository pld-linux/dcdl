%define		fversion	%(echo %{version} |tr . _)
%define		rname	dcd
Summary:	Speech Recognition Decoder Library
Summary(pl):	Biblioteka rozpoznawania dekodowañ
Name:		dcdl
Version:	2.0
Release:	1
License:	Free for non-comercial use, non-distributable
Group:		Applications/Text
# from http://akpublic.research.att.com/cgi-bin/access.cgi/as/vt/ext-software/www-ne-license.cgi?form.dcd.binary
Source0:	%{rname}_%{fversion}.linux.i386.tar.gz
URL:		http://www.research.att.com/sw/tools/dcd/
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DCD Library is a software collection for speech recognition
decoding and related functions. Based on the Finite-State Machine
(FSM) Library, it provides higher-level operations needed specifically
for decoding.

%description -l pl
Biblioteka DCD to zbiór oprogramowania dekodowania i zbli¿onych
funkcji zwi±zanych z rozpoznawaniem mowy. Jest oparta na bibliotece
FSM (automatów skoñczonych), udostêpnia operacje wy¿szego poziomu
potrzebne w szczególno¶ci do dekodowania.

%prep
%setup -q -n %{rname}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man{1,3,5},%{_includedir}}
install bin/* $RPM_BUILD_ROOT%{_bindir}
install doc/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install doc/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
install doc/*.5 $RPM_BUILD_ROOT%{_mandir}/man5
install include/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_includedir}/*
