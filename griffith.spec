%define _version_art	0.9.4

Summary:	Film collection manager application
Name:		griffith
Version:	0.13
Release:	3
License:	GPLv2
Group:		Databases
URL:		http://griffith.cc/
Source:		http://download.berlios.de/griffith/%{name}-%{version}.tar.gz
Source1:	http://download.berlios.de/griffith/%{name}-extra-artwork-%{_version_art}.tar.gz
BuildArch:	noarch
BuildRequires:	docbook-utils
BuildRequires:	python-sqlalchemy
BuildRequires:	pkgconfig(python2)
BuildRequires:	desktop-file-utils
Requires:	python-psycopg2
Requires:	python-chardet
Requires:	python-imaging
Requires:	python-reportlab >= 1.19
Requires:	python-sqlite2
Requires:	python-sqlalchemy
Requires:	pygtk2.0-libglade
Requires:	xpdf

%description
Griffith is a film collection manager application. Adding items to the movie
collection is as quick and easy as typing the film title and selecting a
supported source. Griffith will then try to fetch all the related information
from the Web.

%prep
%setup -q -a 1
%__mv %{name}-extra-artwork-%{_version_art} extra-artwork

%build

%install
%makeinstall_std

%__rm -f %{buildroot}%{_bindir}/%{name}
pushd %{buildroot}%{_bindir}
%__ln_s ../share/%{name}/lib/%{name} .
popd

# extra-artwork
%__install -m 644 extra-artwork/images/* %{buildroot}%{_datadir}/%{name}/images
for i in AUTHORS ChangeLog COPYING; do
	%__mv extra-artwork/$i $i.extra-artwork
done

desktop-file-install --vendor="" \
    --remove-category="Database" \
    --remove-category="GNOME" \
    --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-man

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README INSTALL NEWS TODO *.extra-artwork
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%{_mandir}/man1/griffith.1.*
%config(noreplace) %{_sysconfdir}/bash_completion.d/griffith
