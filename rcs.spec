Summary:	RCS - version control system
Summary(de):	RCS - Versionssteuersystem
Summary(fr):	RCS - Système de contrôle de version
Summary(pl):	RCS - system kontroli wersji
Summary(tr):	Sürüm denetleme sistemi
Name:		rcs
Version:	5.7
Release:	12
Copyright:	GPL
Group:		Development/Version Control
Group(pl):	Programowanie/Zarzadzanie Wersjami
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		rcs-stupidrcs.patch
Patch1:		rcs-DESTDIR.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Revision Control System (RCS) manages multiple revisions of files. RCS
automates the storing, retrieval, logging, identification, and merging of
revisions. RCS is useful for text that is revised frequently, for example
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
%setup  -q
%patch0 -p1
%patch1 -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS \
%configure \
	--with-diffutils
touch src/conf.h
make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	NEWS REFS
 
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
