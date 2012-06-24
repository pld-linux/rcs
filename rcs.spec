Summary:	RCS - version control system
Summary(de):	RCS - Versionssteuersystem
Summary(fr):	RCS - Syst�me de contr�le de version
Summary(pl):	RCS - system kontroli wersji
Summary(tr):	S�r�m denetleme sistemi
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
und das Zusammenf�hren von Revisionen. RCS ist praktisch f�r Texte, die
h�ufig revidiert werden, etwa Programme, Dokumentation, Graphiken, Artikel
und Formulare.

%description -l fr
Le syst�me de contr�le de r�vision (RCS) g�re les nombreuses r�visions des
fichiers. RCS automatise le stockage, la r�cup�ration, l'identification et
le m�lange des r�visions. RCS sert aux textes r�vis�s fr�quemment, par
exemple les "programmes, la documentation, les graphiques, les articles et
les lettres.

%description -l pl
Revision Control System (RCS) - w wolnym t�umaczeniu system kontroli wersji
umo�liwia zarz�dzanie wieloma wersjami plik�w. Za pomoc� RCS mo�na w prosty
spos�b automatyzowa� sk�adowanie, wyci�ganie, logowanie z archiwum jak i
��czenie dokument�w r�nych wersji. RCS jest wygodny do zarz�dzania
dokument�w cz�sto zmienianych jak kod �r�d�owy program�w, dokumentacja,
grafika czy listy.

%description -l tr
S�r�m denetim sistemi (Revision Control System - RCS) bir dosyan�n birden
fazla s�r�m�n� denetlemek i�in kullan�l�r. RCS dosya �zerindeki
de�i�ikliklerin tutulmas�n�, saklanmas�n�, kay�tlar�n�n tutulmas� i�lerini
kolayla�t�r�r. �zerinde s�k�a de�i�iklik yap�lan program kodlar�, belgeler
ve makaleler i�in son derece yararl� bir ara�t�r.

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
