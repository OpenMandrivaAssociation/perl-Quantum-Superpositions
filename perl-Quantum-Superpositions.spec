%define upstream_name    Quantum-Superpositions
%define upstream_version 2.02

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Conjunctive & Disjunctive logic for Perl5
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Quantum/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Class::Multimethods)
BuildRequires: perl(strict)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*


