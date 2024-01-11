Name:           jsch
Version:        0.1.55
Release:        5%{?dist}
Summary:        Pure Java implementation of SSH2
License:        BSD
URL:            http://www.jcraft.com/jsch/
BuildArch:      noarch

Source0:        http://download.sourceforge.net/sourceforge/jsch/jsch-%{version}.zip
# stripped manifest based on 
# https://download.eclipse.org/tools/orbit/downloads/drops2/R20201130205003/repository/plugins/com.jcraft.jsch_0.1.55.v20190404-1902.jar
Source1:        MANIFEST.MF
Source2:        plugin.properties

BuildRequires:  maven-local
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  zip

Requires:       jzlib >= 0:1.0.5

%description
JSch allows you to connect to an sshd server and use port forwarding, 
X11 forwarding, file transfer, etc., and you can integrate its 
functionality into your own Java programs.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
%{summary}.

%prep
%setup -q
%mvn_file : jsch

%pom_remove_parent

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-compiler-plugin

%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_set pom:project/pom:version %{version}

%build
%mvn_build

# inject the OSGi Manifest
mkdir META-INF
cp %{SOURCE1} META-INF
cp %{SOURCE2} plugin.properties
touch META-INF/MANIFEST.MF
touch plugin.properties
zip target/%{name}-%{version}.jar META-INF/MANIFEST.MF
zip target/%{name}-%{version}.jar plugin.properties

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 0.1.55-5
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 29 2021 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.55-4
- Fix maven-compiler-plugin configuration

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 0.1.55-3
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.55-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jan 12 2021 Alexander Kurtakov <akurtako@redhat.com> 0.1.55-1
- Update to latest upstream version.

* Sun Aug 30 2020 Fabio Valentini <decathorpe@gmail.com> - 0.1.54-14
- Remove unnecessary dependency on parent POM.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Jiri Vanek <jvanek@redhat.com> - 0.1.54-12
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.55-3
- Mass rebuild for javapackages-tools 201902

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 24 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.55-2
- Mass rebuild for javapackages-tools 201901

* Mon May 13 2019 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.55-1
- Update to upstream version 0.1.55

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Sep  5 2018 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.54-7
- Remove unneeded maven-compiler-plugin configuration

* Tue Aug 07 2018 Michael Simacek <msimacek@redhat.com> - 0.1.54-8
- Fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 23 2017 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.54-4
- Remove unneeded maven-javadoc-plugin invocation

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.54-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Alexander Kurtakov <akurtako@redhat.com> 0.1.54-2
- Fix version in pom.xml.

* Wed Aug 31 2016 Alexander Kurtakov <akurtako@redhat.com> - 0.1.54-1
- New upstream release 0.1.54

* Wed Jun 15 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 0.1.53-5
- Add missing build-requires

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.53-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.53-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.1.53-2
- Revert jsch.jar to not be in javadir subdir.

* Fri Jun 5 2015 Alexander Kurtakov <akurtako@redhat.com> 0.1.53-1
- Update to 0.1.53
- Build with xmvn.
