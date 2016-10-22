%{?scl:%scl_package google-gson}
%{!?scl:%global pkg_name %{name}}

%{?thermostat_find_provides_and_requires}

%global short_name   gson
%global group_id     com.google.code.gson

Name:             %{?scl_prefix}google-%{short_name}
Version:          2.2.4
Release:          1.3%{?dist}
Summary:          Java lib for conversion of Java objects into JSON representation
License:          ASL 2.0
Group:            Development/Libraries
URL:              http://code.google.com/p/%{pkg_name}
# request for tarball: http://code.google.com/p/google-gson/issues/detail?id=283
# svn export http://google-gson.googlecode.com/svn/tags/gson-%{version} google-gson-%{version}
# tar caf google-gson-%{version}.tar.xz google-gson-%{version}
Source0:          %{pkg_name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    java7-devel
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-enforcer-plugin

Requires:         java
Requires:         jpackage-utils

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Summary:          API documentation for %{name}
Group:            Documentation
Requires:         jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << "EOF"}
%setup -q -n %{pkg_name}-%{version}

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << "EOF"}
# LANG="C" or LANG="en_US.utf8" needed for the tests
mvn-rpmbuild -Dmaven.test.failure.ignore=true package
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << "EOF"}
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{pkg_name}.jar

# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{pkg_name}.pom
%add_maven_depmap JPP-%{pkg_name}.pom %{pkg_name}.jar

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/apidocs/* %{buildroot}%{_javadocdir}/%{name}
%{?scl:EOF}

%files
%doc LICENSE README
%{_javadir}/%{pkg_name}.jar
%{_mavenpomdir}/JPP-%{pkg_name}.pom
%{_mavendepmapfragdir}/%{name}

%files javadoc
%doc LICENSE
%doc %{_javadocdir}/%{name}

%changelog
* Mon Jan 20 2014 Omair Majid <omajid@redhat.com> - 2.2.4-1.3
- Rebuild in order to fix osgi()-style provides.
- Resolves: RHBZ#1054813

* Thu Nov 14 2013 Michal Srb <msrb@redhat.com> - 2.2.4-1.2
- Fix SCL dirs

* Tue Nov 12 2013 Michal Srb <msrb@redhat.com> - 2.2.4-1.1
- Enable SCL for thermostat

* Tue May 14 2013 Alexander Kurtakov <akurtako@redhat.com> 2.2.4-1
- Update to newer upstream release.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.2.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

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
