
# TODO: finish that stuff

# Conditional build:
%bcond_without	dist_kernel	# allow non-distribution kernel
%bcond_without	kernel		# don't build kernel modules
%bcond_without	userspace	# don't build userspace programs
%bcond_with	verbose		# verbose build (V=1)

%if %{without kernel}
%undefine	with_dist_kernel
%endif

#
# main package.
#
%define		rel	0.1
######		Unknown group!
Summary:	Kingsun KS-959 IrDA dongle driver for Linux 2.6.x
Summary(pl.UTF-8):	Sterownik Kingsun KS-959 IrDA  dla Linuxa 2.6.x
Name:		ks-959
Version:	0.1
Release:	%{rel}
Epoch:		0
License:	GPL
Group:		Kernel
##Source0:	%{name}-%{version}.tar.gz
Source0:	http://palosanto.com/~a_villacis/codeprojects/%{name}.tar.bz2
# Source0-md5:	26d42a148095215fe174e90ce5960cce
#Source1:	-
URL:		http://palosanto.com/~a_villacis/codeprojects/kingsun-linux.en.html#ks959
%if %{with kernel}
%{?with_dist_kernel:BuildRequires:	kernel%{_alt_kernel}-module-build >= 3:2.6.20.2}
BuildRequires:	rpmbuild(macros) >= 1.379
%endif
#BuildRequires:	-
#Requires(postun):	-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires:	-
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%description -l pl.UTF-8

# kernel subpackages.

%package -n kernel%{_alt_kernel}-usb-ks959-sir
Summary:	Linux driver for ks959-sir
Summary(pl.UTF-8):	Sterownik dla Linuksa do ks959-sir
Release:	%{rel}@%{_kernel_ver_str}
Group:		Base/Kernel
Requires(post,postun):	/sbin/depmod
%if %{with dist_kernel}
%requires_releq_kernel
Requires(postun):	%releq_kernel
%endif

%description -n kernel%{_alt_kernel}-usb-ks959-sir
Kingsun KS-959 IrDA dongle driver for Linux 2.6.x This dongle is
(currently) a SIR-only device, and supports speed from 2400 to 57600
bps. This package contains Linux module.

%description -n kernel%{_alt_kernel}-usb-ks959-sir -l pl.UTF-8
Sterownik Linuksa 2.6.x dla Kingsun KS-959 IrDA. Aktualnie
obsługiwany jest tylko tryb SIR w prędkościach od 2400 do 57600
bps. Ten pakiet zawiera moduł jądra Linuksa.

%prep
%setup -n %{name}
# prepare makefile:
# cat > path/to/dir/Makefile << EOF
cat > Makefile << 'EOF'

obj-m += ks959-sir.o

%{?debug:CFLAGS += -DCONFIG_ks959-sir_DEBUG=1}
EOF

%build
%if %{with userspace}


%endif

%if %{with kernel}
%build_kernel_modules -m ks959-sir

# modules placed in subdirectory:
%build_kernel_modules -C ks-959 -m ks959-sir


%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with userspace}


%endif

%if %{with kernel}
%install_kernel_modules -m ks959-sir -d kernel/drivers/usb

# to avoid conflict with in-kernel modules, and prepare modprobe config:
%install_kernel_modules -s current -n NAME -m ks959-sir -d kernel/drivers/usb
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-n kernel%{_alt_kernel}-usb-ks959-sir
%depmod %{_kernel_ver}

%postun	-n kernel%{_alt_kernel}-usb-ks959-sir
%depmod %{_kernel_ver}

%if %{with kernel}
%files -n kernel%{_alt_kernel}-usb-ks959-sir
%defattr(644,root,root,755)
/lib/modules/%{_kernel_ver}/kernel/drivers/usb/*.ko*
%endif

%if %{with userspace}
%files
%defattr(644,root,root,755)

%endif
