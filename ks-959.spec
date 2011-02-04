#
# TODO: finish that stuff
#
# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_with	verbose		# verbose build (V=1)
#
%define		rel	1
%define		mod_name	ks959-sir
Summary:	Kingsun KS-959 IrDA dongle driver for Linux 2.6.x
Summary(pl.UTF-8):	Sterownik Kingsun KS-959 IrDA dla Linuksa 2.6.x
Name:		ks-959
Version:	0.1
Release:	%{rel}
Epoch:		0
License:	GPL
Group:		Base/Kernel
Source0:	http://palosanto.com/~a_villacis/codeprojects/%{name}.tar.bz2
# Source0-md5:	26d42a148095215fe174e90ce5960cce
URL:		http://palosanto.com/~a_villacis/codeprojects/kingsun-linux.en.html#ks959
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2}
BuildRequires:	rpmbuild(macros) >= 1.379
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kingsun KS-959 IrDA dongle driver for Linux 2.6.x. This dongle is
(currently) a SIR-only device, and supports speed from 2400 to 57600
bps.

%description -l pl.UTF-8
Sterownik dla Linuksa 2.6.x do dongle'a IrDA Kingsun KS-959. Aktualnie
obsługiwany jest tylko tryb SIR z prędkościami od 2400 do 57600
bps.

%package -n kernel%{_alt_kernel}-usb-%{mod_name}
Summary:	Kingsun KS-959 IrDA dongle driver for Linux 2.6.x
Summary(pl.UTF-8):	Sterownik Kingsun KS-959 IrDA dla Linuksa 2.6.x
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-usb-%{mod_name}
Kingsun KS-959 IrDA dongle driver for Linux 2.6.x. This dongle is
(currently) a SIR-only device, and supports speed from 2400 to 57600
bps.

%description -n kernel%{_alt_kernel}-usb-%{mod_name} -l pl.UTF-8
Sterownik dla Linuksa 2.6.x do dongle'a IrDA Kingsun KS-959. Aktualnie
obsługiwany jest tylko tryb SIR z prędkościami od 2400 do 57600
bps.

%prep
%setup -n %{name}

%build
%build_kernel_modules -m %{mod_name}

%install
rm -rf $RPM_BUILD_ROOT

%install_kernel_modules -m %{mod_name} -d kernel/drivers/usb

%clean
rm -rf $RPM_BUILD_ROOT

%post -n kernel%{_alt_kernel}-usb-%{mod_name}
%depmod %{_kernel_ver}

%postun -n kernel%{_alt_kernel}-usb-%{mod_name}
%depmod %{_kernel_ver}

%files -n kernel%{_alt_kernel}-usb-%{mod_name}
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/drivers/usb/ks959-sir.ko*
