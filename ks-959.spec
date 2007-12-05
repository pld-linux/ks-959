
# TODO: finish that stuff

# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)

#
# main package.
#
%define		rel	0.1
%define		_mod_name	ks959-sir
Summary:	Kingsun KS-959 IrDA dongle driver for Linux 2.6.x
Summary(pl.UTF-8):	Sterownik Kingsun KS-959 IrDA  dla Linuxa 2.6.x
Name:		kernel%{_alt_kernel}-usb-ks959-sir
Version:	0.1
Release:	%{rel}
Epoch:		0
License:	GPL
Group:		Kernel
Source0:	http://palosanto.com/~a_villacis/codeprojects/ks-959.tar.bz2
# Source0-md5:	26d42a148095215fe174e90ce5960cce
URL:		http://palosanto.com/~a_villacis/codeprojects/kingsun-linux.en.html#ks959
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2}
BuildRequires:	rpmbuild(macros) >= 1.379
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kingsun KS-959 IrDA dongle driver for Linux 2.6.x This dongle is
(currently) a SIR-only device, and supports speed from 2400 to 57600
bps. This package contains Linux module.

%description -l pl.UTF-8
Sterownik Linuksa 2.6.x dla Kingsun KS-959 IrDA. Aktualnie
obsługiwany jest tylko tryb SIR w prędkościach od 2400 do 57600
bps. Ten pakiet zawiera moduł jądra Linuksa.

%prep
%setup -n ks-959

%build
%build_kernel_modules -m %{_mod_name}

%install
rm -rf $RPM_BUILD_ROOT

%install_kernel_modules -m %{_mod_name} -d kernel/drivers/usb

%clean
rm -rf $RPM_BUILD_ROOT

%post
%depmod %{_kernel_ver}

%postun
%depmod %{_kernel_ver}

%files 
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/drivers/usb/*.ko*
