%global short_name   gson
%global group_id     com.google.code.gson

%global pkg_name google-%{short_name}
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

Name:             %{?scl_prefix}%{pkg_name}

Version:          2.2.4
Release:          1%{?dist}
Summary:          Java lib for conversion of Java objects into JSON representation
License:          ASL 2.0
Group:            Development/Libraries
URL:              https://github.com/google/gson
Source0:          https://github.com/google/gson/archive/gson-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    java-1.7.0-openjdk-devel
BuildRequires:    %{?scl_prefix}maven-local
BuildRequires:    %{?scl_prefix_maven}maven-surefire-provider-junit
BuildRequires:    %{?scl_prefix_maven}maven-install-plugin
BuildRequires:    %{?scl_prefix_maven}maven-enforcer-plugin

Requires:         java
%{?scl:Requires: %scl_runtime}

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%prep
%setup -q -n gson-gson-%{version}

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE

scl enable %{scl_maven} %{scl} - <<"EOF"
%mvn_file : %{pkg_name}
EOF

%build
scl enable %{scl_maven} %{scl} - <<"EOF"
# LANG="C" or LANG="en_US.utf8" needed for the tests
%mvn_build -fj
EOF

%install
scl enable %{scl_maven} %{scl} - <<"EOF"
%mvn_install
EOF

%files -f .mfiles
%doc LICENSE README

%changelog
* Mon Jan 09 2017 Michael Simacek <msimacek@redhat.com> - 2.2.4-1
- Update to upstream version 2.2.4
- Resolves: rhbz#1401037

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.2.2-8.3
- Mass rebuild 2015-01-13

* Fri Jan 09 2015 Michal Srb <msrb@redhat.com> - 2.2.2-8.2
- Mass rebuild 2015-01-09

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.2.2-8.1
- Migrate to mvn_build

* Tue Dec 16 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.2-8
- Migrate requires and build-requires to rh-java-common

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.2-7
- Mass rebuild 2014-12-15

* Mon Dec 15 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.2.2-6
- Rebuild for rh-java-common collection

* Tue May 27 2014 Sami Wagiaalla <swagiaal@redhat.com>  2.2.2-5
- Enable maven scl for add_maven_depmap.

* Fri May 23 2014 Sami Wagiaalla <swagiaal@redhat.com>  2.2.2-5
- Add missing maven deps.

* Thu May 22 2014 Sami Wagiaalla <swagiaal@redhat.com>  2.2.2-5
- build for DTS 3

* Thu Apr 4 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.2.2-4
- Drop R dependency to java 7.
- Drop javadoc subpackage.

* Mon Feb 18 2013 Krzysztof Daniel <kdaniel@redhat.com> 2.2.2-3
- Initial contribution to SCL.

* Wed Dec 19 2012 Severin Gehwolf <sgehwolf@redhat.com> 2.2.2-2
- Add BR for surefire junit provider.

* Wed Dec 19 2012 Severin Gehwolf <sgehwolf@redhat.com> 2.2.2-1
- Update to latest upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 2 2012 Alexander Kurtakov <akurtako@redhat.com> 2.2.1-2
- Add missing BR on maven-enforcer-plugin.
- Remove no longer needed parts of the spec.

* Mon Jul 2 2012 Krzysztof Daniel <kdaniel@redhat.com> 2.2.1-1
- Update to latest upstream 2.2.1

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 13 2011 Jaromir Capik <jcapik@redhat.com> - 1.7.1-3
- Removal of failing testInetAddressSerializationAndDeserialization

* Wed May 11 2011 Jaromir Capik <jcapik@redhat.com> - 1.7.1-2
- Conversion of CR+LF to LF in the license file

* Tue May 10 2011 Jaromir Capik <jcapik@redhat.com> - 1.7.1-1
- Initial version of the package
