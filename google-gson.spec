%global short_name   gson

%{?scl:%scl_package google-%{short_name}}
%{!?scl:%global pkg_name %{name}}

%global group_id     com.google.code.gson

# Exclude generation of osgi() style provides, since they are not
# SCL-namespaced and may conflict with base RHEL packages.
# See: https://bugzilla.redhat.com/show_bug.cgi?id=1045433
%global __provides_exclude ^osgi(.*)$

Name:             %{?scl_prefix}google-%{short_name}
Version:          2.2.4
Release:          8%{?dist}
Summary:          Java lib for conversion of Java objects into JSON representation
License:          ASL 2.0
Group:            Development/Libraries
URL:              http://code.google.com/p/%{pkg_name}
# request for tarball: http://code.google.com/p/google-gson/issues/detail?id=283
# svn export http://google-gson.googlecode.com/svn/tags/gson-%{version} google-gson-%{version}
# tar caf google-gson-%{version}.tar.xz google-gson-%{version}
Source0:          %{pkg_name}-%{version}.tar.xz

BuildArch:        noarch

BuildRequires:    java-devel
BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-install-plugin

Requires:         java
Requires:         jpackage-utils

%{?scl:Requires: %scl_runtime}

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
%mvn_build -- -Dmaven.test.failure.ignore=true
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_javadir}/%{name}

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jan 27 2014 Severin Gehwolf <sgehwolf@redhat.com> - 2.2.4-8
- Own scl-ized google-gson directory in javadir.
- Resolves: RHBZ#1057169

* Fri Dec 20 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-7
- Don't generate osgi() style provides.
- Resolves: RHBZ#1045433.

* Wed Nov 27 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-6
- Properly enable SCL.

* Wed Nov 06 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-5
- Use xmvn.

* Tue Sep 24 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-4
- Bump release for rebuild.

* Tue Sep 17 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-3
- Add BR maven-install-plugin.

* Wed Aug 28 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-2
- SCL-ize package.

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
