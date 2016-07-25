%{?scl:%scl_package google-gson}
%{!?scl:%global pkg_name %{name}}

%{?thermostat_find_provides_and_requires}

%global short_name   gson
%global group_id     com.google.code.gson

Name:             %{?scl_prefix}google-%{short_name}
Version:          2.2.4
# Release should be higher than el7 builds. Use convention
# 60.X where X is an increasing int. 60 for rhel-6. We use
# 70.X for rhel-7. For some reason we cannot rely on the
# dist tag.
Release:          60.2%{?dist}
Summary:          Java lib for conversion of Java objects into JSON representation
License:          ASL 2.0
Group:            Development/Libraries
URL:              http://code.google.com/p/%{pkg_name}
# request for tarball: http://code.google.com/p/google-gson/issues/detail?id=283
# svn export http://google-gson.googlecode.com/svn/tags/gson-%{version} google-gson-%{version}
# tar caf google-gson-%{version}.tar.xz google-gson-%{version}
Source0:          %{pkg_name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    maven30-maven-local
BuildRequires:    maven30-maven-surefire-provider-junit
BuildRequires:    maven30-maven-enforcer-plugin

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Summary:          API documentation for %{name}
Group:            Documentation

%description javadoc
This package contains the API documentation for %{name}.

%prep
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%setup -q -n %{pkg_name}-%{version}

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - << "EOF"}
# LANG="C" or LANG="en_US.utf8" needed for the tests
%mvn_build -- -Dmaven.test.failure.ignore=true
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - << "EOF"}
%mvn_install
# Own the gson directory in order to avoid it sticking
# around after removal
install -d -m 755 %{buildroot}%{_javadir}/google-gson
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE README
# Own the gson directory in order to avoid it sticking
# around after removal
%dir %{_javadir}/google-gson

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Fri Jun 20 2014 Severin Gehwolf <sgehwolf@redhat.com> - 2.2.4-60.2
- Own google-gson directory in scl.

* Fri Jun 20 2014 Severin Gehwolf <sgehwolf@redhat.com> - 2.2.4-60.1
- Build using the maven30 collection.
- Use maven-local macros.

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
