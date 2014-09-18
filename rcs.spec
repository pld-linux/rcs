Summary:	RCS - version control system
Summary(de.UTF-8):	RCS - Versionssteuersystem
Summary(es.UTF-8):	RCS - sistema de control de versiones
Summary(fr.UTF-8):	RCS - Système de contrôle de version
Summary(pl.UTF-8):	RCS - system kontroli wersji
Summary(pt_BR.UTF-8):	RCS - sistema de controle de versões
Summary(tr.UTF-8):	Sürüm denetleme sistemi
Name:		rcs
Version:	5.9.3
Release:	1
License:	GPL v3+
Group:		Development/Version Control
Source0:	http://ftp.gnu.org/gnu/rcs/%{name}-%{version}.tar.xz
# Source0-md5:	855fc9b65dba143d7da304e63baf93a9
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	ba094b833436afc14ac1679a78e50da5
Patch0:		%{name}-debian.patch
Patch1:		%{name}-info.patch
URL:		http://www.cs.purdue.edu/homes/trinkle/RCS/
BuildRequires:	groff
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Revision Control System (RCS) manages multiple revisions of files.
RCS automates the storing, retrieval, logging, identification, and
merging of revisions. RCS is useful for text that is revised
frequently, for example programs, documentation, graphics, papers, and
form letters.

%description -l de.UTF-8
Das Revision Control Syste (RCS) verwaltet mehrere Dateirevisionen. Es
automatisiert das Abspeichern, das Einlesen, das Aufzeichnen, die
Erkennung und das Zusammenführen von Revisionen. RCS ist praktisch für
Texte, die häufig revidiert werden, etwa Programme, Dokumentation,
Graphiken, Artikel und Formulare.

%description -l es.UTF-8
Sistema de Control de Revisión (RCS) administra múltiples revisiones
de archivos. RCS automatiza el almacenamiento, recuperación, registro,
identificación y la fusión de revisiones. Es útil para textos se
revisan frecuentemente, como programas, documentación, gráficos y
formularios de cartas.

%description -l fr.UTF-8
Le système de contrôle de révision (RCS) gère les nombreuses révisions
des fichiers. RCS automatise le stockage, la récupération,
l'identification et le mélange des révisions. RCS sert aux textes
révisés fréquemment, par exemple les "programmes, la documentation,
les graphiques, les articles et les lettres.

%description -l pl.UTF-8
Revision Control System (RCS) - w wolnym tłumaczeniu system kontroli
wersji umożliwia zarządzanie wieloma wersjami plików. Za pomocą RCS
można w prosty sposób automatyzować składowanie, wyciąganie, logowanie
z archiwum jak i łączenie dokumentów różnych wersji. RCS jest wygodny
do zarządzania dokumentów często zmienianych jak kod źródłowy
programów, dokumentacja, grafika czy listy.

%description -l pt_BR.UTF-8
O Sistema de Controle de Revisão (RCS) administra múltiplas revisões
de arquivos. RCS automatiza o armazenamento, recuperação, registro,
identificação e a fusão de revisões. RCS é útil para texto que é
revisado freqüentemente, como programas, documentação, gráficos e
formulários de cartas.

%description -l tr.UTF-8
Sürüm denetim sistemi (Revision Control System - RCS) bir dosyanın
birden fazla sürümünü denetlemek için kullanılır. RCS dosya üzerindeki
değişikliklerin tutulmasını, saklanmasını, kayıtlarının tutulması
işlerini kolaylaştırır. Üzerinde sıkça değişiklik yapılan program
kodları, belgeler ve makaleler için son derece yararlı bir araçtır.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-mailer=/usr/lib/sendmail

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}
%{__rm} $RPM_BUILD_ROOT%{_mandir}/*/man1/rcsfreeze.1*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/README.rcs-non-english-man-pages

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/ci
%attr(755,root,root) %{_bindir}/co
%attr(755,root,root) %{_bindir}/ident
%attr(755,root,root) %{_bindir}/merge
%attr(755,root,root) %{_bindir}/rcs
%attr(755,root,root) %{_bindir}/rcsclean
%attr(755,root,root) %{_bindir}/rcsdiff
%attr(755,root,root) %{_bindir}/rcsmerge
%attr(755,root,root) %{_bindir}/rlog
%{_mandir}/man1/ci.1*
%{_mandir}/man1/co.1*
%{_mandir}/man1/ident.1*
%{_mandir}/man1/merge.1*
%{_mandir}/man1/rcs.1*
%{_mandir}/man1/rcsclean.1*
%{_mandir}/man1/rcsdiff.1*
%{_mandir}/man1/rcsmerge.1*
%{_mandir}/man1/rlog.1*
%{_mandir}/man5/rcsfile.5*
%lang(fi) %{_mandir}/fi/man[15]/*
%lang(ja) %{_mandir}/ja/man[15]/*
%lang(pl) %{_mandir}/pl/man[15]/*
%{_infodir}/rcs.info*
