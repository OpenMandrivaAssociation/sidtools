%define name sidtools
%define version 1.0.1
%define release %mkrel 6


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
/sbin/ldconfig
%_install_info sidtools.info

%postun
/sbin/ldconfig
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

