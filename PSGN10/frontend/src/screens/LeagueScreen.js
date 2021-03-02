import React, { useState, useEffect } from 'react';
import BaseScreen from "./BaseScreen";
import CustomSelect from "../form-elements/Select";
import DatePickerSingle from '../components/DatePickerSingle/DatePickerSingle'
import { Table } from "antd";
import { Typography } from 'antd';
import { Row, Col } from 'antd';
import axios from "axios";

export default function LeagueScreen(props) {
    const [fixtures, setFixtures] = useState([]);
    const [leagues, setLeagues] = useState([]);
    const [seasons, setSeasons] = useState([]);
    const { Title } = Typography;

    useEffect( () => {
        axios
            .get("/core/fixtures/all/")
            .then(response => {
                setFixtures(response.data)
            })
            .finally(() => {
            })
        axios
            .get("/core/season/all/")
            .then(response => {
                setSeasons(response.data)
            })
            .finally(() => {
            })
        axios
            .get("/core/league/all/")
            .then(response => {
                setLeagues(response.data)
            })
            .finally(() => {
            })

    }, []);

    const columns = [
       {
        title: '',
        dataIndex: 'time',
        key: 'time',
      },
      {
        title: '',
        dataIndex: 'teamA',
        key: 'teamA',
      },
      {
        title: '',
        dataIndex: 'teamB',
        key: 'teamB',
      },
    ];

    return (
        <BaseScreen>
            <div className="league-header-container">
                <Row>
                    <Col span={6}>

                    </Col>
                    <Col span={12}>
                        <Row>
                            <Col span={12}>
                                <CustomSelect options={seasons} placeholder="Select a Season"/>
                            </Col>
                            <Col span={12}>
                                <CustomSelect options={leagues} placeholder="Select a League"/>
                            </Col>
                        </Row>
                        <Table columns={columns} dataSource={fixtures} />
                        <div className="">
                            <Title level={3}>LaLiga Fixtures</Title>
                        </div>

                        <DatePickerSingle />


                    </Col>

                    <Col span={6}>

                    </Col>
                </Row>
            </div>
        </BaseScreen>
    )
}



