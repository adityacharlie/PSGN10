import { Select } from 'antd';

export default function CustomSelect(props){
    const { Option } = Select;
    const { options } = props;

    function onChange(value) {
        console.log(`selected ${value}`);
    }

    return (
        <Select
            showSearch
            style={{ width: 200 }}
            placeholder="Select a League"
            optionFilterProp="children"
            onChange={onChange}
            filterOption={(input, option) =>
              option.children.toLowerCase().indexOf(input.toLowerCase()) >= 0
            }
          >

            {
                options.map(each => {
                    return (
                        <Option value="{each.season}">{each.season}</Option>
                    )
                })
            }
          </Select>
    )
}