Summary:	RCS - version control system
Summary(es):	RCS - sistema de control de versiones
Summary(de):	RCS - Versionssteuersystem
Summary(fr):	RCS - Système de contrôle de version
Summary(pl):	RCS - system kontroli wersji
Summary(pt_BR):	RCS - sistema de controle de versões
Summary(tr):	Sürüm denetleme sistemi
Name:		rcs
Version:	5.7
Release:	20
License:	GPL
Group:		Development/Version Control
Source0:	ftp://ftp.gnu.org/pub/gnu/rcs/%{name}-%{version}.tar.gz
# Source0-md5:	4c8e896f2d2446fa593c6f1601a4fb75
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	ba094b833436afc14ac1679a78e50da5
Patch0:		%{name}-stupidrcs.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-security.patch
URL:		http://www.cs.purdue.edu/homes/trinkle/RCS/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Revision Control System (RCS) manages multiple revisions of files.
RCS automates the storing, retrieval, logging, identification, and
merging of revisions. RCS is useful for text that is revised
frequently, for example programs, documentation, graphics, papers, and
form letters.

%description -l de
Das Revision Control Syste (RCS) verwaltet mehrere Dateirevisionen. Es
automatisiert das Abspeichern, das Einlesen, das Aufzeichnen, die
Erkennung und das Zusammenführen von Revisionen. RCS ist praktisch für
Texte, die häufig revidiert werden, etwa Programme, Dokumentation,
Graphiken, Artikel und Formulare.

%description -l es
Sistema de Control de Revisión (RCS) administra múltiples revisiones
de archivos. RCS automatiza el almacenamiento, recuperación, registro,
identificación y la fusión de revisiones. Es útil para textos se
revisan frecuentemente, como programas, documentación, gráficos y
formularios de cartas.

%description -l fr
Le système de contrôle de révision (RCS) gère les nombreuses révisions
des fichiers. RCS automatise le stockage, la récupération,
l'identification et le mélange des révisions. RCS sert aux textes
révisés fréquemment, par exemple les "programmes, la documentation,
les graphiques, les articles et les lettres.

%description -l pl
Revision Control System (RCS) - w wolnym t³umaczeniu system kontroli
wersji umo¿liwia zarz±dzanie wieloma wersjami plików. Za pomoc± RCS
mo¿na w prosty sposób automatyzowaæ sk³adowanie, wyci±ganie, logowanie
z archiwum jak i ³±czenie dokumentów ró¿nych wersji. RCS jest wygodny
do zarz±dzania dokumentów czêsto zmienianych jak kod ¼ród³owy
programów, dokumentacja, grafika czy listy.

%description -l pt_BR
O Sistema de Controle de Revisão (RCS) administra múltiplas revisões
de arquivos. RCS automatiza o armazenamento, recuperação, registro,
identificação e a fusão de revisões. RCS é útil para texto que é
revisado freqüentemente, como programas, documentação, gráficos e
formulários de cartas.

%description -l tr
Sürüm denetim sistemi (Revision Control System - RCS) bir dosyanýn
birden fazla sürümünü denetlemek için kullanýlýr. RCS dosya üzerindeki
deðiþikliklerin tutulmasýný, saklanmasýný, kayýtlarýnýn tutulmasý
iþlerini kolaylaþtýrýr. Üzerinde sýkça deðiþiklik yapýlan program
kodlarý, belgeler ve makaleler için son derece yararlý bir araçtýr.

%prep
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure \
	--with-diffutils
touch src/conf.h
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
rm -f $RPM_BUILD_ROOT%{_mandir}/*/man1/rcsfreeze.1*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS REFS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
%lang(fi) %{_mandir}/fi/man[15]/*
%lang(ja) %{_mandir}/ja/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
