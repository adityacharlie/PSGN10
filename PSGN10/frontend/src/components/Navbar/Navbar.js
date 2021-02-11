import { PureComponent } from 'react';
import { connect } from 'react-redux';
import { Layout, Menu, Breadcrumb } from 'antd';
import { logoutUser } from "../../actions/AuthActions";
import './Navbar.css';

const { Header, Content, Footer } = Layout;

class Navbar extends PureComponent {

  render() {

    const { isLoggedIn, logoutUser} = this.props

    console.log(isLoggedIn, logoutUser);
    return (
      <Layout>
        <Header style={{ position: 'fixed', zIndex: 1, width: '100%' }}>
          <div className="logo" />
          <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
            <Menu.Item key="summary">Summary</Menu.Item>
            <Menu.Item key="fixtures">Fixtures</Menu.Item>
            <Menu.Item key="team_statistics">Team Statistics</Menu.Item>
            <Menu.Item key="player_statistics">Player Statistics</Menu.Item>
          </Menu>
        </Header>
        <Content className="site-layout" style={{ padding: '0 50px', marginTop: 64 }}>
          <Breadcrumb style={{ margin: '16px 0' }}>
            <Breadcrumb.Item>Home</Breadcrumb.Item>
            <Breadcrumb.Item>List</Breadcrumb.Item>
            <Breadcrumb.Item>App</Breadcrumb.Item>
          </Breadcrumb>
          <div className="site-layout-background" style={{ padding: 24, minHeight: 380 }}>
            Content
          </div>
        </Content>
        <Footer>Data sources - Getty Images. Copyright © 2021 CharlieDigital.com</Footer>
      </Layout>
    );
  }
}
const mapStateToProps = state => {
    return {
        user: state.auth.user,
        isLoggedIn: state.auth.isLoggedIn,
    }
}

export default  connect(
    mapStateToProps,
    { logoutUser }
)(Navbar)