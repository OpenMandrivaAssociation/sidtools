%define name sidtools
%define version 1.0.1
%define release: 11


Name: %{name}
Summary: Creates and plays playlists for Sidplay
Version: %{version}
Release: %{release}
License: GPL
Group: Sound
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source: http://user.tninet.se/~uxm165t/%{name}-%{version}.tar.bz2
URL: http://user.tninet.se/~uxm165t/sidtools.html
Requires: sidplay-base

%description
A set of tools to create playlists (and play them) for SidPlay.  Lists
can be created automatically, via the search engine search2list, or
manually, with a text editor.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build

%configure

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_install_info sidtools.info

%postun
%_remove_install_info sidtools.info

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog NEWS AUTHORS THANKS TODO
%config(noreplace) %{_sysconfdir}/sidtoolsrc
%{_infodir}/sidtools.info*
%{_bindir}/sidplayo
%{_bindir}/search2list
%{_bindir}/makelist
%{_bindir}/sidlist



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-10mdv2010.0
+ Revision: 433782
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-9mdv2009.0
+ Revision: 260672
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-8mdv2009.0
+ Revision: 252433
- rebuild
- fix no-buildroot-tag

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.1-6mdv2008.1
+ Revision: 127255
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import sidtools


* Tue Apr 26 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-6mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-5mdk
- rebuild

* Mon Jan 27 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-4mdk
- rebuild

* Thu Oct 10 2002  Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-3mdk
- rebuild

* Mon Sep 03 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-2mdk
- rebuild

* Fri May 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.1-1mdk
- updated by Götz Waschk <waschk@linux-mandrake.com> :
	- 1.0.1
	- remove obsoleted patch

* Wed May  2 2001 Götz Waschk <waschk@linux-mandrake.com> 1.0-2mdk
- added default config file
- added requirement for sidplay-base
- cosmetics

* Wed Oct 11 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0-1mdk
- used srpm from Götz Waschk <waschk@linux-mandrake.com> :
	Wed Oct 11 2000 Götz Waschk <waschk@linux-mandrake.com> 1.0-1mdk
	1.0

* Thu Oct 05 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-1mdk
- used srpm from Götz Waschk :
	Wed Oct  4 2000 Götz Waschk <waschk@linux-mandrake.com> 0.9.1-1mdk
	- initial Mandrake build

