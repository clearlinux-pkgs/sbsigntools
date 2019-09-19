#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : sbsigntools
Version  : 0.9.1
Release  : 6
URL      : https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/snapshot/sbsigntools-0.9.1.tar.gz
Source0  : https://git.kernel.org/pub/scm/linux/kernel/git/jejb/sbsigntools.git/snapshot/sbsigntools-0.9.1.tar.gz
Source1  : https://github.com/rustyrussell/ccan/archive/b1f28e17227f2320d07fe052a8a48942fe17caa5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 MIT
Requires: sbsigntools-bin = %{version}-%{release}
Requires: sbsigntools-license = %{version}-%{release}
Requires: sbsigntools-man = %{version}-%{release}
BuildRequires : binutils-dev
BuildRequires : gnu-efi
BuildRequires : gnu-efi-dev
BuildRequires : gnu-efi-staticdev
BuildRequires : help2man
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(uuid)

%description
sbsigntool - Signing utility for UEFI secure boot
See file ./INSTALL for building and installation instructions.

%package bin
Summary: bin components for the sbsigntools package.
Group: Binaries
Requires: sbsigntools-license = %{version}-%{release}

%description bin
bin components for the sbsigntools package.


%package license
Summary: license components for the sbsigntools package.
Group: Default

%description license
license components for the sbsigntools package.


%package man
Summary: man components for the sbsigntools package.
Group: Default

%description man
man components for the sbsigntools package.


%prep
%setup -q -n sbsigntools-0.9.1
cd ..
%setup -q -T -D -n sbsigntools-0.9.1 -b 1
mkdir -p lib/ccan.git
cp -r %{_topdir}/BUILD/ccan-b1f28e17227f2320d07fe052a8a48942fe17caa5/* %{_topdir}/BUILD/sbsigntools-0.9.1/lib/ccan.git

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1568882172
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1568882172
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/sbsigntools
cp COPYING %{buildroot}/usr/share/package-licenses/sbsigntools/COPYING
cp LICENSE.GPLv3 %{buildroot}/usr/share/package-licenses/sbsigntools/LICENSE.GPLv3
cp lib/ccan.git/ccan/alloc/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_alloc_LICENSE
cp lib/ccan.git/ccan/antithread/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_antithread_LICENSE
cp lib/ccan.git/ccan/asearch/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_asearch_LICENSE
cp lib/ccan.git/ccan/asort/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_asort_LICENSE
cp lib/ccan.git/ccan/asprintf/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_asprintf_LICENSE
cp lib/ccan.git/ccan/autodata/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_autodata_LICENSE
cp lib/ccan.git/ccan/avl/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_avl_LICENSE
cp lib/ccan.git/ccan/bdelta/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_bdelta_LICENSE
cp lib/ccan.git/ccan/block_pool/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_block_pool_LICENSE
cp lib/ccan.git/ccan/btree/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_btree_LICENSE
cp lib/ccan.git/ccan/cast/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_cast_LICENSE
cp lib/ccan.git/ccan/ccan_tokenizer/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ccan_tokenizer_LICENSE
cp lib/ccan.git/ccan/charset/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_charset_LICENSE
cp lib/ccan.git/ccan/ciniparser/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ciniparser_LICENSE
cp lib/ccan.git/ccan/crc/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_crc_LICENSE
cp lib/ccan.git/ccan/crcsync/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_crcsync_LICENSE
cp lib/ccan.git/ccan/daemon_with_notify/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_daemon_with_notify_LICENSE
cp lib/ccan.git/ccan/daemonize/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_daemonize_LICENSE
cp lib/ccan.git/ccan/darray/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_darray_LICENSE
cp lib/ccan.git/ccan/dgraph/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_dgraph_LICENSE
cp lib/ccan.git/ccan/endian/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_endian_LICENSE
cp lib/ccan.git/ccan/failtest/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_failtest_LICENSE
cp lib/ccan.git/ccan/foreach/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_foreach_LICENSE
cp lib/ccan.git/ccan/grab_file/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_grab_file_LICENSE
cp lib/ccan.git/ccan/htable/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_htable_LICENSE
cp lib/ccan.git/ccan/idtree/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_idtree_LICENSE
cp lib/ccan.git/ccan/ilog/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ilog_LICENSE
cp lib/ccan.git/ccan/iscsi/LICENCE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_iscsi_LICENCE
cp lib/ccan.git/ccan/iscsi/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_iscsi_LICENSE
cp lib/ccan.git/ccan/jmap/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_jmap_LICENSE
cp lib/ccan.git/ccan/jset/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_jset_LICENSE
cp lib/ccan.git/ccan/json/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_json_LICENSE
cp lib/ccan.git/ccan/lbalance/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_lbalance_LICENSE
cp lib/ccan.git/ccan/likely/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_likely_LICENSE
cp lib/ccan.git/ccan/list/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_list_LICENSE
cp lib/ccan.git/ccan/md4/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_md4_LICENSE
cp lib/ccan.git/ccan/net/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_net_LICENSE
cp lib/ccan.git/ccan/nfs/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_nfs_LICENSE
cp lib/ccan.git/ccan/objset/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_objset_LICENSE
cp lib/ccan.git/ccan/ogg_to_pcm/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ogg_to_pcm_LICENSE
cp lib/ccan.git/ccan/opt/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_opt_LICENSE
cp lib/ccan.git/ccan/ptr_valid/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ptr_valid_LICENSE
cp lib/ccan.git/ccan/rbtree/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_rbtree_LICENSE
cp lib/ccan.git/ccan/read_write_all/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_read_write_all_LICENSE
cp lib/ccan.git/ccan/sparse_bsearch/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_sparse_bsearch_LICENSE
cp lib/ccan.git/ccan/str_talloc/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_str_talloc_LICENSE
cp lib/ccan.git/ccan/stringmap/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_stringmap_LICENSE
cp lib/ccan.git/ccan/talloc/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_talloc_LICENSE
cp lib/ccan.git/ccan/talloc_link/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_talloc_link_LICENSE
cp lib/ccan.git/ccan/tally/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_tally_LICENSE
cp lib/ccan.git/ccan/time/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_time_LICENSE
cp lib/ccan.git/ccan/tlist/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_tlist_LICENSE
cp lib/ccan.git/ccan/ttxml/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ttxml_LICENSE
cp lib/ccan.git/ccan/typesafe_cb/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_typesafe_cb_LICENSE
cp lib/ccan.git/ccan/wwviaudio/LICENSE %{buildroot}/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_wwviaudio_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sbattach
/usr/bin/sbkeysync
/usr/bin/sbsiglist
/usr/bin/sbsign
/usr/bin/sbvarsign
/usr/bin/sbverify

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/sbsigntools/COPYING
/usr/share/package-licenses/sbsigntools/LICENSE.GPLv3
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_alloc_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_antithread_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_asearch_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_asort_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_asprintf_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_autodata_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_avl_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_bdelta_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_block_pool_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_btree_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_cast_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ccan_tokenizer_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_charset_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ciniparser_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_crc_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_crcsync_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_daemon_with_notify_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_daemonize_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_darray_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_dgraph_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_endian_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_failtest_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_foreach_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_grab_file_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_htable_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_idtree_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ilog_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_iscsi_LICENCE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_iscsi_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_jmap_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_jset_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_json_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_lbalance_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_likely_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_list_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_md4_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_net_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_nfs_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_objset_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ogg_to_pcm_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_opt_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ptr_valid_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_rbtree_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_read_write_all_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_sparse_bsearch_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_str_talloc_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_stringmap_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_talloc_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_talloc_link_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_tally_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_time_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_tlist_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_ttxml_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_typesafe_cb_LICENSE
/usr/share/package-licenses/sbsigntools/lib_ccan.git_ccan_wwviaudio_LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/sbattach.1
/usr/share/man/man1/sbsiglist.1
/usr/share/man/man1/sbsign.1
/usr/share/man/man1/sbvarsign.1
/usr/share/man/man1/sbverify.1
