Name: 		amide
Version: 	1.0.1
Release: 	1
Summary: 	Program for viewing and analyzing medical image data sets
License: 	GPLv2+
Group: 		Graphics
URL: 		http://amide.sourceforge.net
Source0: 	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Patch0:		amide-1.0.1-mdv-format-security.patch

BuildRequires:  xmedcon-devel
BuildRequires:  volpack-devel 
BuildRequires:  libxml2-devel 
#BuildRequires:  gtk-doc 
BuildRequires:  gnome-doc-utils
BuildRequires:  pkgconfig(libgnomecanvas-2.0)
BuildRequires:  ffmpeg-devel >= 0.4.9
BuildRequires:  gsl-devel
BuildRequires:  dcmtk-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel >= 2.10
BuildRequires:	gnome-vfs2-devel
BuildRequires:	intltool

%description 

AMIDE is a tool for viewing and analyzing medical image data sets.
It's capabilities include the simultaneous handling of multiple data
sets imported from a variety of file formats, image fusion, 3D region
of interest drawing and analysis, volume rendering, and rigid body
alignments.


%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	   --enable-gtk-doc=yes \
	   --enable-libecat=no \
	   --enable-amide-debug=no \
	   --disable-scrollkeeper
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

desktop-file-install --vendor gnome --delete-original                   \
  --dir %{buildroot}%{_datadir}/applications                         \
  --add-category X-Red-Hat-Extra                                        \
  %{buildroot}%{_datadir}/applications/*

rm -rf %{buildroot}/var/scrollkeeper

%find_lang %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README todo
%{_bindir}/*
%{_datadir}/pixmaps
%{_datadir}/gnome
%{_datadir}/omf
%{_datadir}/applications
%{_datadir}/gtk-doc
%{_mandir}/man1/*



