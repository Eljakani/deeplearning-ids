import React, { useState, useEffect } from 'react';
import { Layout, Menu, Breadcrumb, Progress, Statistic } from 'antd';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';
import Dashboard from './Dashboard';

const { Header, Content, Footer } = Layout;
const { Countdown } = Statistic;

const App = () => {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [dashboardData, setDashboardData] = useState({
    lineChartData: [],
    networkTraffic: 0,
    detectedThreats: 0,
  });

  useEffect(() => {
    
  }, []);

  const renderContent = () => {
    switch (activeTab) {
      case 'dashboard':
        return (
          <Dashboard />
        );
      case 'alerts':
        return <div>Alerts Content</div>;
      case 'settings':
        return <div>Settings Content</div>;
      default:
        return null;
    }
  };

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ position: 'fixed', zIndex: 1, width: '100%' }}>
        <div className="logo" />
        <Menu
          theme="dark"
          mode="horizontal"
          selectedKeys={[activeTab]}
          onClick={(e) => setActiveTab(e.key)}
        >
          <Menu.Item key="dashboard">Dashboard</Menu.Item>
          <Menu.Item key="alerts">Alerts</Menu.Item>
          <Menu.Item key="settings">Settings</Menu.Item>
        </Menu>
      </Header>
      <Content
        className="site-layout"
        style={{ padding: '0 50px', marginTop: 64 }}
      >
        <Breadcrumb style={{ margin: '16px 0' }}>
          <Breadcrumb.Item>Network IDS Monitoring</Breadcrumb.Item>
          <Breadcrumb.Item>{activeTab.charAt(0).toUpperCase() + activeTab.slice(1)}</Breadcrumb.Item>
        </Breadcrumb>
        <div
          className="site-layout-background"
          style={{ padding: 24, minHeight: 380 }}
        >
          {renderContent()}
        </div>
      </Content>
      <Footer style={{ textAlign: 'center' }}>
        Network IDS Monitoring ©2024
      </Footer>
    </Layout>
  );
};

export default App;