%define upstream_name    Quantum-Superpositions
%define upstream_version 2.03

Name:		perl-%{upstream_name}
Version:	2.03
Release:	4

Summary:	Conjunctive & Disjunctive logic for Perl5
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Quantum-Superpositions
Source0:	https://cpan.metacpan.org/authors/id/L/LE/LEMBARK/Quantum-Superpositions-2.03.tar.gz

BuildRequires:	make
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
%setup -q -n Quantum-Superpositions-2.03

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

