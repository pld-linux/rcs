Summary:	RCS - version control system
Summary(es):	RCS - sistema de control de versiones
Summary(de):	RCS - Versionssteuersystem
Summary(fr):	RCS - Syst�me de contr�le de version
Summary(pl):	RCS - system kontroli wersji
Summary(pt_BR):	RCS - sistema de controle de vers�es
Summary(tr):	S�r�m denetleme sistemi
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
Erkennung und das Zusammenf�hren von Revisionen. RCS ist praktisch f�r
Texte, die h�ufig revidiert werden, etwa Programme, Dokumentation,
Graphiken, Artikel und Formulare.

%description -l es
Sistema de Control de Revisi�n (RCS) administra m�ltiples revisiones
de archivos. RCS automatiza el almacenamiento, recuperaci�n, registro,
identificaci�n y la fusi�n de revisiones. Es �til para textos se
revisan frecuentemente, como programas, documentaci�n, gr�ficos y
formularios de cartas.

%description -l fr
Le syst�me de contr�le de r�vision (RCS) g�re les nombreuses r�visions
des fichiers. RCS automatise le stockage, la r�cup�ration,
l'identification et le m�lange des r�visions. RCS sert aux textes
r�vis�s fr�quemment, par exemple les "programmes, la documentation,
les graphiques, les articles et les lettres.

%description -l pl
Revision Control System (RCS) - w wolnym t�umaczeniu system kontroli
wersji umo�liwia zarz�dzanie wieloma wersjami plik�w. Za pomoc� RCS
mo�na w prosty spos�b automatyzowa� sk�adowanie, wyci�ganie, logowanie
z archiwum jak i ��czenie dokument�w r�nych wersji. RCS jest wygodny
do zarz�dzania dokument�w cz�sto zmienianych jak kod �r�d�owy
program�w, dokumentacja, grafika czy listy.

%description -l pt_BR
O Sistema de Controle de Revis�o (RCS) administra m�ltiplas revis�es
de arquivos. RCS automatiza o armazenamento, recupera��o, registro,
identifica��o e a fus�o de revis�es. RCS � �til para texto que �
revisado freq�entemente, como programas, documenta��o, gr�ficos e
formul�rios de cartas.

%description -l tr
S�r�m denetim sistemi (Revision Control System - RCS) bir dosyan�n
birden fazla s�r�m�n� denetlemek i�in kullan�l�r. RCS dosya �zerindeki
de�i�ikliklerin tutulmas�n�, saklanmas�n�, kay�tlar�n�n tutulmas�
i�lerini kolayla�t�r�r. �zerinde s�k�a de�i�iklik yap�lan program
kodlar�, belgeler ve makaleler i�in son derece yararl� bir ara�t�r.

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
