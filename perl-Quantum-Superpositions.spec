%define upstream_name    Quantum-Superpositions
%define upstream_version 2.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Conjunctive & Disjunctive logic for Perl5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Quantum/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Class::Multimethods)
BuildRequires:	perl(strict)
BuildArch:	noarch

%description
The Quantum::Superpositions module adds two new operators to Perl: 'any'
and 'all'.

Each of these operators takes a list of values (states) and superimposes
them into a single scalar value (a superposition), which can then be stored
in a standard scalar variable.

The 'any' and 'all' operators produce two distinct kinds of superposition.
The 'any' operator produces a disjunctive superposition, which may
(notionally) be in any one of its states at any time, according to the
needs of the algorithm that uses it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 2.20.0-2mdv2011.0
+ Revision: 654290
- rebuild for updated spec-helper

* Thu May 06 2010 Michael Scherer <misc@mandriva.org> 2.20.0-1mdv2011.0
+ Revision: 542892
- import perl-Quantum-Superpositions


* Thu May 06 2010 cpan2dist 2.02-1mdv
- initial mdv release, generated with cpan2dist
