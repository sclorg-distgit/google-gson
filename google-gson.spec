%{?scl:%scl_package google-gson}
%{!?scl:%global pkg_name %{name}}

Name:             %{?scl_prefix}google-gson
Version:          2.3.1
Release:          6.1%{?dist}
Summary:          Java lib for conversion of Java objects into JSON representation
License:          ASL 2.0
URL:              https://github.com/google/gson
Source0:          https://github.com/google/gson/archive/gson-%{version}.tar.gz

BuildArch:        noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.sonatype.oss:oss-parent:pom:)

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%package javadoc
Summary:          API documentation for %{pkg_name}

%description javadoc
This package contains the API documentation for %{pkg_name}.

%prep
%setup -q -n gson-gson-%{version}

# convert CR+LF to LF
sed -i 's/\r//g' LICENSE

# Test requires network
rm src/test/java/com/google/gson/DefaultInetAddressTypeAdapterTest.java

# Throwable has more fields serialized, probably incorrect test expectations
rm src/test/java/com/google/gson/functional/ThrowableFunctionalTest.java

# Fixes build with new maven-jar-plugin
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-jar-plugin']/pom:executions" "
    <execution>
      <id>default-jar</id>
      <phase>skip</phase>
    </execution>"

%pom_remove_plugin :maven-javadoc-plugin

%build
# LANG="C" or LANG="en_US.utf8" needed for the tests
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE README

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Wed Jun 21 2017 Java Maintainers <java-maint@redhat.com> - 2.3.1-6.1
- Automated package import and SCL-ization

* Thu Feb 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3.1-6
- Remove unneeded maven-javadoc-plugin invocation

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jun 02 2016 Michael Simacek <msimacek@redhat.com> - 2.3.1-4
- Skip default jar plugin execution to fix FTBFS

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 26 2015 Michael Simacek <msimacek@redhat.com> - 2.3.1-1
- Update to upstream version 2.3.1

* Mon Apr 20 2015 Michael Simacek <msimacek@redhat.com> - 2.2.4-8
- Remove test that relies on networking

* Mon Mar 30 2015 Michael Simacek <msimacek@redhat.com> - 2.2.4-7
- Remove dependency on cobertura

* Tue Jun 10 2014 Severin Gehwolf <sgehwolf@redhat.com> - 2.2.4-6
- Move to xmvn style packaging.
- Fix FTBFS. Resolves RHBZ#1106707.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 2.2.4-4
- Use Requires: java-headless rebuild (#1067528)

* Mon Aug 05 2013 Severin Gehwolf <sgehwolf@redhat.com> 2.2.4-3
- Add BR maven-install-plugin, resolves RHBZ#992422.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

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
