Summary:	RCS - version control system
Summary(de):	RCS - Versionssteuersystem
Summary(fr):	RCS - Système de contrôle de version
Summary(pl):	RCS - system kontroli wersji
Summary(tr):	Sürüm denetleme sistemi
Name:		rcs
Version:	5.7
Release:	11
Copyright:	GPL
Group:		Development/Version Control
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch:		rcs-stupidrcs.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
The Revision Control System (RCS) manages multiple revisions of files. RCS
automates the storing, retrieval, logging, identification, and merging of
revisions.  RCS is useful for text that is revised frequently, for example
programs, documentation, graphics, papers, and form letters.

%description -l de
Das Revision Control Syste (RCS) verwaltet mehrere Dateirevisionen.  Es
automatisiert das Abspeichern, das Einlesen, das Aufzeichnen, die Erkennung
und das Zusammenführen von Revisionen. RCS ist praktisch für Texte, die
häufig revidiert werden, etwa Programme, Dokumentation, Graphiken, Artikel
und Formulare.

%description -l fr
Le système de contrôle de révision (RCS) gère les nombreuses révisions des
fichiers. RCS automatise le stockage, la récupération, l'identification et
le mélange des révisions. RCS sert aux textes révisés fréquemment, par
exemple les "programmes, la documentation, les graphiques, les articles et
les lettres.

%description -l pl
Revision Control System (RCS) - w wolnym t³umaczeniu system kontroli wersji
umo¿liwia zarz±dzanie wieloma wersjami plików. Za pomoc± RCS mo¿na w prosty
sposób automatyzowaæ sk³adowanie, wyci±ganie, logowanie z archiwum jak i
³±czenie dokumentów ró¿nych wersji. RCS jest wygodny do zarz±dzania
dokumentów czêsto zmienianych jak kod ¼ród³owy programów, dokumentacja,
grafika czy listy.

%description -l tr
Sürüm denetim sistemi (Revision Control System - RCS) bir dosyanýn birden
fazla sürümünü denetlemek için kullanýlýr. RCS dosya üzerindeki
deðiþikliklerin tutulmasýný, saklanmasýný, kayýtlarýnýn tutulmasý iþlerini
kolaylaþtýrýr. Üzerinde sýkça deðiþiklik yapýlan program kodlarý, belgeler
ve makaleler için son derece yararlý bir araçtýr.

%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr \
	--with-diffutils
touch src/conf.h
make 

%install
rm -rf $RPM_BUILD_ROOT
make install prefix=$RPM_BUILD_ROOT/usr

gzip -9nf $RPM_BUILD_ROOT/usr/man/man*/* \
	NEWS REFS
 
%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) /usr/bin/*
/usr/man/man[15]/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Apr  1 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [5.7-11]
- removed man group from man pages,
- gzipped %doc.

* Thu Oct 01 1998 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [5.7-8d]
- fixed ELF binaries permissions,
- added %defattr support,
- build against Tornado,
- minor modifications of the spec file.

* Sun Aug  2 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [5.7-8]
- added pl translation,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added -q %setup parameter,
- added using %%{name} and %%{version} macro in Source,
- "rm -rf $RPM_BUILD_ROOT" moved from %prep to %install,
- simplification in %install,
- added %defattr and %attr macros in %files (allows building package from
  non-root account).

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Wed Oct 21 1997 Cristian Gafton <gafton@redhat.com>
- fixed the spec file; added BuildRoot

* Fri Jul 18 1997 Erik Troan <ewt@redhat.com>
- built against glibc
